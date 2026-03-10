from enum import Enum
from colorama import Fore as fc, Style as st


class ItemType(Enum):
    CONSUMABLE = "Consumable"
    KEY_ITEM = "Key Item"


class Item:
    def __init__(self, item_id, name, item_type, description="", quantity=1, reusable=False):
        self.id = item_id
        self.name = name
        self.item_type = item_type
        self.description = description
        self.quantity = quantity
        self.reusable = reusable


class Consumable(Item):
    def __init__(self, item_id, name, description="", quantity=1, reusable=False, effect=None):
        super().__init__(item_id, name, ItemType.CONSUMABLE, description, quantity, reusable)
        self.effect = effect or {}

    def use(self, player):
        if "health" in self.effect:
            amount = self.effect["health"]
            player.damage(-amount)
            if amount > 0:
                print(f"\n{fc.GREEN}You used {fc.CYAN}{self.name}{fc.GREEN}. (+{amount} HP){fc.RESET}")
            else:
                print(f"\n{fc.RED}You used {fc.CYAN}{self.name}{fc.RED}. ({amount} HP){fc.RESET}")
        if not self.reusable:
            self.quantity -= 1
        return self.quantity <= 0


class KeyItem(Item):
    def __init__(self, item_id, name, description="", quantity=1):
        super().__init__(item_id, name, ItemType.KEY_ITEM, description, quantity, reusable=False)


class Inventory:
    def __init__(self):
        self._items = {}

    def add(self, item_id, quantity=1):
        if item_id in self._items:
            self._items[item_id].quantity += quantity
        else:
            item = create_item(item_id)
            item.quantity = quantity
            self._items[item_id] = item
        item = self._items[item_id]
        print(f"\n<< {fc.CYAN}{item.name}{fc.RESET} has been added to your inventory. >>")

    def remove(self, item_id, quantity=1):
        if item_id not in self._items:
            return
        name = self._items[item_id].name
        self._items[item_id].quantity -= quantity
        if self._items[item_id].quantity <= 0:
            del self._items[item_id]
        print(f"<< {fc.CYAN}{name}{fc.RESET} has been removed from your inventory. >>")

    def has(self, item_id):
        return item_id in self._items

    def __contains__(self, item_id):
        return self.has(item_id)

    def get(self, item_id):
        return self._items.get(item_id)

    def use(self, item_id, player):
        item = self._items.get(item_id)
        if not item or not isinstance(item, Consumable):
            print(f"\n{fc.RED}You can't use that.{fc.RESET}")
            return False
        should_remove = item.use(player)
        if should_remove:
            del self._items[item_id]
        return True

    def get_consumables(self):
        return [item for item in self._items.values() if isinstance(item, Consumable)]

    def get_key_items(self):
        return [item for item in self._items.values() if isinstance(item, KeyItem)]

    def display(self):
        key_items = self.get_key_items()
        consumables = self.get_consumables()
        if not key_items and not consumables:
            print(f"\n{fc.YELLOW}Your inventory is empty.{fc.RESET}")
            return
        if key_items:
            print(f"\n{fc.YELLOW}--- Key Items ---{fc.RESET}")
            for item in key_items:
                print(f"  {fc.CYAN}{item.name}{fc.RESET} - {item.description}")
        if consumables:
            print(f"\n{fc.YELLOW}--- Consumables ---{fc.RESET}")
            for item in consumables:
                effect_str = ""
                if "health" in item.effect:
                    amt = item.effect["health"]
                    effect_str = f" [{fc.GREEN}+{amt} HP{fc.RESET}]" if amt > 0 else f" [{fc.RED}{amt} HP{fc.RESET}]"
                qty = f" (x{item.quantity})" if item.quantity > 1 else ""
                print(f"  {fc.CYAN}{item.name}{fc.RESET}{qty} - {item.description}{effect_str}")


ITEM_CATALOG = {
    # Keys
    "square_key":    {"name": "Square Key",    "type": "key", "description": "A key with a square-shaped head."},
    "circle_key":    {"name": "Circle Key",    "type": "key", "description": "A key with a circle-shaped head."},
    "triangle_key":  {"name": "Triangle Key",  "type": "key", "description": "A key with a triangle-shaped head."},
    "diamond_key":   {"name": "Diamond Key",   "type": "key", "description": "A key with a diamond-shaped head."},
    "cross_key":     {"name": "Cross Key",     "type": "key", "description": "A key with a cross-shaped head."},
    "club_key":      {"name": "Club Key",      "type": "key", "description": "A key shaped like a club."},
    "heart_key":     {"name": "Heart Key",     "type": "key", "description": "A heart-shaped key."},
    "spade_key":     {"name": "Spade Key",     "type": "key", "description": "The final key."},
    "poseidon_key":  {"name": "Poseidon Key",  "type": "key", "description": "A key bearing the mark of the sea god."},
    "handcuff_key":  {"name": "Handcuff Key",  "type": "key", "description": "A small key that fits handcuffs."},
    # Tools
    "damaged_screwdriver": {"name": "Damaged Screwdriver", "type": "key", "description": "A worn-out flat head screwdriver."},
    "serrated_knife":      {"name": "Serrated Knife",      "type": "key", "description": "A sharp knife with a serrated blade."},
    "bolt_cutters":        {"name": "Bolt Cutters",        "type": "key", "description": "Heavy-duty bolt cutters."},
    "slingshot":           {"name": "Slingshot",            "type": "key", "description": "A slingshot with a few pebbles."},
    # Puzzle items
    "artwork_slab": {"name": "Artwork Slab", "type": "key", "description": "A mysterious slab with artwork on it."},
    "diary_page":   {"name": "Diary Page",   "type": "key", "description": "A torn page from someone's diary."},
    # Food
    "banana":          {"name": "Banana",          "type": "consumable", "description": "A ripe banana.",            "effect": {"health": 10}},
    "apple":           {"name": "Apple",           "type": "consumable", "description": "A crisp apple.",            "effect": {"health": 10}},
    "orange":          {"name": "Orange",          "type": "consumable", "description": "A juicy orange.",           "effect": {"health": 10}},
    "bottle_of_water": {"name": "Bottle of Water", "type": "consumable", "description": "A refreshing bottle of water.", "effect": {"health": 15}},
    # Medical
    "painkillers": {"name": "Painkillers", "type": "consumable", "description": "Pain relief medication.",            "effect": {"health": 20}},
    "peroxide":    {"name": "Peroxide",    "type": "consumable", "description": "Hydrogen peroxide for wounds.",      "effect": {"health": 15}},
    "bandage":     {"name": "Bandage",     "type": "consumable", "description": "A roll of bandage.",                 "effect": {"health": 15}},
    "antidote":    {"name": "Antidote",    "type": "consumable", "description": "A vial of antidote.",                "effect": {"health": 30}},
    "snack_bar":   {"name": "Snack Bar",   "type": "consumable", "description": "A tasty snack bar.",                 "effect": {"health": 10}},
    # Special
    "black_potion": {"name": "Black Potion", "type": "consumable", "description": "A deathly black potion.", "effect": {"health": -40}},
}


def create_item(item_id):
    if item_id not in ITEM_CATALOG:
        raise ValueError(f"Unknown item: {item_id}")
    data = ITEM_CATALOG[item_id]
    if data["type"] == "key":
        return KeyItem(item_id, data["name"], data.get("description", ""))
    elif data["type"] == "consumable":
        return Consumable(item_id, data["name"], data.get("description", ""), effect=data.get("effect", {}))
    raise ValueError(f"Unknown item type: {data['type']}")

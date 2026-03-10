from colorama import Fore as fc, Style as st

#Player Class
class player():
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
        self.inventory = []
        self.location = ""
        self.status = []
    def damage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.status = "Dead"
            game_over()
        elif self.health > 100:
            self.health = 100
            print(f"\n\n{fc.GREEN}(Max HP reached!){fc.RESET} ")
        return self.health
    #Display Status
    def display_status(self):
        print(f"\nYou have {fc.RED}{player.health}{fc.RESET} HP remaining.\n\nYour current location is {fc.YELLOW}{player.location}{fc.RESET}.\n\nCurrent keys in your inventory: ")
        for i in player.inventory:
            if 'Key' in i:
                print(f"- {fc.CYAN}{i}{fc.RESET}")
            else:
                continue
        idlechoice()
    #Add to Inventory
    def add_inventory_item(self, item):
        self.inventory.append(item)
        print(f"\n<< {fc.CYAN}{item}{fc.RESET} has been added to your inventory. >>")
    #Remove from Inventory
    def remove_inventory_item(self, item):
        self.inventory.remove(item)
        print(f"<< {fc.CYAN}{item}{fc.RESET} has been removed from your inventory. >>")


#PROLOGUE/Initialize variables
name = input(f"\n\n{fc.BLACK}Please enter your name!{fc.RESET}\n")
name = name.title()
player = player(name)
print(f"\n\n{fc.RED}*****************PROLOGUE*****************{fc.RESET}\n\nYou are a person named {fc.BLUE}{player.name}{fc.RESET} who has been wandering in the woods for hours.\nYou escaped from a prisoner transport on your way to Goh Rahn prison as the sun went down.\n{fc.MAGENTA}You still have the handcuffs on you.{fc.RESET}\nYou managed to swipe a backpack from one of the guards during your escape, but it didn't have a lot of supplies in it.\nYou ran out of food and water a while ago, and you're starting to feel hungry.\nYou're sure you heard that there was a shack out here that is always full of supplies...\n...but you can't find it anywhere. Your throat starts feeling dry, and your stomach growls...\n\n{fc.RED}-----------------SOME AMOUNT OF TIME LATER-----------------{fc.RESET}\n\nAfter wandering around for what felt like an eternity, you find a clearing you're sure was not there before.\nYou pass through the clearing, and see the silhouette of a rundown shack.\nYou carefully approach the silhouette of the shack, closely inspecting the ground with each step you take.\nYou hear a noise that startles you as you take a step.\n{fc.MAGENTA}You activate a bear trap, and shriek in pain.{fc.RESET} ({fc.RED}-75 HP{fc.RESET})"); {player.damage(75)}; print(f"Thankfully, you still have that flat head screwdriver in your backpack, but it's a little worn out.")
player.add_inventory_item('Damaged Screwdriver')
player.status.append('shackled')
input(f"\nYou start to jimmy the latch on the bear trap with the screwdriver.\nAfter a bit of struggle, you successfully release the bear trap, but feel the screwdriver bending.\nIt definitely won't last much longer.\nYou let out a sigh of relief, followed by a grunt of pain.\nYou head straight for the shack, limping more and more with each step you take.\nYou reach for the handle...\n\n{fc.RED}{st.BRIGHT}------------------------------------------------------------------\n*****   *    *      *       ****   *     *   *      *****   *****\n*       *    *     * *     *       *   *     *      *       *    *\n*****   ******    *   *    *       ****      *      *****   *    *\n    *   *    *   *******   *       *   *     *      *       *    *\n*****   *    *  *       *   ****   *     *   *****  *****   *****\n------------------------------------------------------------------{fc.RESET}{st.NORMAL}\n\n(Press ENTER to continue your adventure...) ")
player.location = "the Entrance"
rug_visited = False
hatch_revealed = False
slab_placed = False
artwork_visited = False
west_door_accessed = False
north_door_accessed = False
east_door_accessed = False
desk_drawer_unlocked = False
desk_drawer_looted = False
end_bottom_visited = False
end_table_visited = False
desk_approached = False
bookcase_visited = False
bookcase_looted = False
yellow_book_discovered = False
fridge_looted = False
chair_broken = False
loose_brick = False
square_puzzle = False
circle_puzzle = False
triangle_puzzle = False
cross_puzzle = False
podiums_visited = False
seven_keys = False
all_keys = False
golden_podium_visited = False


#Game Over
def game_over():
    print(f"{fc.RED}\n\n...you should have been more careful...\n...now you will forever be... \n...{st.BRIGHT}SHACKLED{st.NORMAL}...\n\n### G A M E   O V E R ###{fc.RESET}")
    quit()


#Check inventory for keys
def key_check():
    global seven_keys
    if seven_keys == True:
        return seven_keys
    elif seven_keys == False:
        if 'Square Key' in player.inventory and 'Circle Key' in player.inventory and 'Triangle Key' in player.inventory and 'Cross Key' in player.inventory and 'Club Key' in player.inventory and 'Heart Key' in player.inventory and 'Diamond Key' in player.inventory:
            seven_keys = True
        else:
            seven_keys = False


#Idle function
def idlechoice():
    choice = input(f"\n\n{fc.BLACK}What would you like to do? (1:Enter another room  2:Search current room  3:Check status){fc.RESET} ")
    acceptable = ['1','2','3']
    while choice not in acceptable:
        choice = input(f"{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Enter another room  2:Search current room  3:Check status) {fc.RESET}")
    if choice == '1':
        changerooms()
    elif choice == '2':
        roomscan()
    elif choice == '3':
        player.display_status()  


#Inspect Diary Page
def inspect_page():
    print(f"\nYou inspect the page.\n\n<February 15, 1989>\n\n\nToday is the best day of my life.\n\nI finally figured out how to escape from the Devil!\nThe {fc.CYAN}key{fc.RESET} will be revealed upon controlling the {fc.BLUE}God of the Sea{fc.RESET} with mastery of the {fc.GREEN}four{fc.RESET} elements of the human body.\n\nThe {fc.BLACK}{st.BRIGHT}mind{fc.RESET}{st.NORMAL}, represented by the {fc.BLACK}{st.BRIGHT}shovel{fc.RESET}{st.NORMAL}...\nThe {fc.YELLOW}body{fc.RESET}, represented by the {fc.YELLOW}clover{fc.RESET}...\nThe {fc.RED}heart{fc.RESET} that represents {fc.RED}itself{fc.RESET}...\nAnd the {fc.MAGENTA}{st.BRIGHT}soul{fc.RESET}{st.NORMAL}, represented by {fc.MAGENTA}{st.BRIGHT}riches{fc.RESET}{st.NORMAL}...\n\nThe {fc.MAGENTA}{st.BRIGHT}soul{fc.RESET}{st.NORMAL} should be mastered before the {fc.RED}heart{fc.RESET}.\n\nThe {fc.BLUE}God of the Sea{fc.RESET} should be tamed before mastering the {fc.YELLOW}body{fc.RESET}.\n\nThe {fc.BLACK}{st.BRIGHT}mind{fc.RESET}{st.NORMAL} is mastered in the end.\n\nOnly one who masters the {fc.GREEN}four{fc.RESET} elements of the human body, taming the {fc.BLUE}God of the Sea{fc.RESET} along the way, can escape from this hell...\n\n{fc.RED}It's too late for me...{fc.RESET}\n\n{fc.BLACK}<< end >>{fc.RESET}")


#Western Room Status
def west_status():
    global slab_placed
    global west_door_accessed
    if slab_placed == True and west_door_accessed == True:
        return "unlocked"
    elif slab_placed == True and west_door_accessed == False:
        return True
    else:
        return False


#Northern Room Status
def north_status():
    global north_door_accessed
    if north_door_accessed == True:
        return True
    else:
        return False


#Eastern Room Status
def east_status():
    global east_door_accessed
    if east_door_accessed == True:
        return True
    else:
        return False


#KEY ITEM CHECKS
def square_key():
    if "Square Key" not in player.inventory:
        print(f"\n{fc.GREEN}You have found the Square Key!{fc.RESET}")
        player.add_inventory_item('Square Key')
    elif "Square Key" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Square Key{fc.RESET}.\n\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def circle_key():
    if "Circle Key" not in player.inventory:
        print(f"\nYou reach for the top shelf and grab a metal tin.\nYou give it a little rattle, and hear something inside.\n\n{fc.GREEN}You open the tin to find a key!{fc.RESET}")
        player.add_inventory_item('Circle Key')
    elif "Circle Key" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Circle Key{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def triangle_and_diamond_key():
    if "Triangle Key" not in player.inventory:
        print(f"\nYou open the top drawer.\nThe same picture of the beautiful woman from earlier is in here.\n\n{fc.GREEN}You lift the picture to find two keys!{fc.RESET}")
        player.add_inventory_item('Diamond Key')
        player.add_inventory_item('Triangle Key')
    elif "Triangle Key" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Triangle Key{fc.RESET} and {fc.CYAN}Diamond Key{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def cross_key():
    if "Cross Key" not in player.inventory:
        print(f"\nYou slash open the spine of the book with your {fc.CYAN}Serrated Knife{fc.RESET}.\n\n{fc.GREEN}There was a key hidden inside!{fc.RESET}")
        player.add_inventory_item('Cross Key')
    elif "Cross Key" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Cross Key{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def spade_key():
    if "Spade Key" not in player.inventory:
        print(f"\nThis mysterious lock box has many differently-shaped key holes.\nYou count seven.")
        print(f"\nUsing all seven other Suit and Shape keys, you unlock the lock box.\n\n{fc.GREEN}You have found the final key!{fc.RESET}")
        player.add_inventory_item('Spade Key')
    elif "Spade Key" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Spade Key{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def club_key():
    if "Club Key" not in player.inventory:
        print(f"\nYou pull out your slingshot and take aim.\nYou fire the pebble you found with it straight at the fake lightbulb.\nAs you suspected, the fake bulb gets knocked loose and shatters on the floor!\n\n{fc.GREEN}You find a key on the floor where the fake bulb shattered!{fc.RESET}")
        player.add_inventory_item('Club Key')
    elif "Club Key" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Club Key{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def heart_key():
    if "Heart Key" not in player.inventory:
        print(f"\n{fc.GREEN}You found a heart-shaped key!{fc.RESET}")
        player.add_inventory_item('Heart Key')
    elif "Heart Key" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Heart Key{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def poseidon_key():
    if "Poseidon Key" not in player.inventory:
        print(f"\nYou hear a strange noise from above as you hit the fourth button and shield your head with your hands.\nA loose brick falls from the ceiling and shatters on the floor.\n\n{fc.GREEN}It had a key inside!{fc.RESET}")
        player.add_inventory_item('Poseidon Key')
    elif "Poseidon Key" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Poseidon's Key{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def handcuff_key():
    if "Handcuff Key" not in player.inventory:
        print(f"\n{fc.GREEN}You reach down and grab the key!{fc.RESET}")
        player.add_inventory_item('Handcuff Key')
        print(f"\nYou recognize this key to be one made for handcuffs.\nYou try your luck...\n\n{fc.GREEN}Your handcuffs have been removed!{fc.RESET}")
        player.status.remove('shackled')
        player.status.append('unshackled')
    elif "Handcuff Key" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Handcuff Key{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def artwork_slab():
    if "Artwork Slab" not in player.inventory:
        print(f"\nYou open the drawer to find what appears to be a slab of wooden artwork.\n{fc.GREEN}You grab the strange slab of wood.{fc.RESET}")
        player.add_inventory_item('Artwork Slab')
    elif "Artwork Slab" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Artwork Slab{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def serrated_knife():
    if "Serrated Knife" not in player.inventory:
        print(f"\nYou approach the bed.\nIt's a plain wire-frame bed with a sad little pillow on it.\nThere is no blanket in sight.\nYou lift the pillow to find a knife with very sharp teeth hiding underneath it.\nYou carefully place it in your backpack for later.")
        player.add_inventory_item('Serrated Knife')
    elif "Serrated Knife" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Serrated Knife{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def slingshot():
    if "Slingshot" not in player.inventory:
        print(f"\nYou approach the strange object in the corner of the room.\n\n{fc.GREEN}It is a slingshot with a few pebbles that you could use for ammo!{fc.RESET}")
        player.add_inventory_item('Slingshot')
    elif "Slingshot" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Slingshot{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def boltcutters():
    if "Bolt Cutters" not in player.inventory:
        print(f"\nYou check the bottom shelf of the shelving unit.\nYou find some bolt cutters!")
        player.add_inventory_item('Bolt Cutters')
    elif "Bolt Cutters" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Bolt Cutters{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

def diary_page():
    if "Diary Page" not in player.inventory:
        print(f"\nYou remove the folded page from the back of the photo.\nAfter a quick glance, you think it might have come from a diary...")
        player.add_inventory_item('Diary Page')
        inspect_page()
        return
    elif "Diary Page" in player.inventory:
        print(f"\nThis is the location where you found the {fc.CYAN}Diary Page{fc.RESET}.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")

#Enter another room function
def changerooms():
    global west_door_accessed
    global north_door_accessed
    global east_door_accessed
    global seven_keys
    #ENTRANCE
    if player.location == "the Entrance":
        choice = input(f"\nYou see 3 doors. One each on the Western, Northern, and Eastern walls.\n\n{fc.BLACK}Which room would you like to try to enter? (1:Western  2:Northern  3:Eastern){fc.RESET} ")
        acceptable = ['1','2','3']
        while choice not in acceptable:
            choice = input(f"{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which room would you like to try to enter? (1:Western  2:Northern  3:Eastern){fc.RESET} ")
        if choice == '1' and west_status() == False:
            print(f"\nYou try the knob on the Western door. {fc.RED}It feels jammed.{fc.RESET}")
            idlechoice()
        elif choice == '1' and west_status() == True:
            dec = input(f"\nYou try the knob on the Western door. {fc.GREEN}It's unlocked!{fc.RESET}\n\n{fc.BLACK}Enter the room? (y/n){fc.RESET} ")
            dec = dec.lower()
            acceptable = ['y','n']
            while dec not in acceptable:
                dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Enter the room? (y/n){fc.RESET} ")
                dec = dec.lower()
            if dec == 'y':
                print(f"\nYou enter {fc.YELLOW}the Western room{fc.RESET}.")
                player.location = "the Western room"
                west_door_accessed = True
                west_status()
                idlechoice()
            elif dec == 'n':
                print(f"\nYou have decided to remain in {fc.YELLOW}the Entrance{fc.RESET}.")
                idlechoice()
        elif choice == '1' and west_status() == "unlocked":
            print(f"\nYou enter the door and return to {fc.YELLOW}the Western room{fc.RESET}.")
            player.location = 'the Western room'
            idlechoice()
        elif choice == '2' and 'Bolt Cutters' not in player.inventory:
            print(f"\n{fc.RED}The door is chained shut.{fc.RESET}\n\nSince you have nothing to break these chains, {fc.YELLOW}you decide to come back later{fc.RESET}.")
            idlechoice()
        elif choice == '2' and 'Bolt Cutters' in player.inventory and north_status() == False:
            dec = input(f"\n{fc.RED}The door is chained shut.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Use bolt cutters  2:Never mind){fc.RESET} ")
            acceptable = ['1','2']
            while dec not in acceptable:
                dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Use bolt cutters  2:Never mind){fc.RESET} ")
            if dec == '1':
                north_door_accessed = True
                north_status()
                dec = input(f"\n{fc.GREEN}You have successfully removed the chains from the door!{fc.RESET}\n\nYou try the knob on the door.\n\n{fc.GREEN}It's unlocked!{fc.RESET}\n\n{fc.BLACK}Enter the room? (y/n){fc.RESET} ")
                acceptable = ['y','n']
                while dec not in acceptable:
                    dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Enter the room? (y/n){fc.RESET} ")
                if dec == 'y':
                    print(f"\n\nYou enter {fc.YELLOW}the Northern room{fc.RESET}.")
                    player.location = "the Northern room"
                    idlechoice()
                elif dec == 'n':
                    print(f"\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                    idlechoice()
        elif choice == '2' and north_status() == True:
                print(f"\nYou enter the door and return to {fc.YELLOW}the Northern room{fc.RESET}.")
                player.location = "the Northern room"
                idlechoice()
        elif choice == '3' and east_status() == False:
            unlock = input(f"\nYou try the knob on the Eastern door.\nIt's locked, but you notice a strange design above the keyhole.\n{fc.BLUE}You could swear that it looks like a trident...{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Unlock the door  2:Check status  3:Never mind){fc.RESET} ")
            acceptable = ['1','2','3']
            while unlock not in acceptable:
                unlock = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Unlock the door  2:Check status  3:Never mind){fc.RESET} ")
            if unlock == '1' and "Poseidon Key" in player.inventory:
                east_door_accessed = True
                east_status()
                dec = input(f"\n{fc.GREEN}You have unlocked the door!{fc.RESET}\n\n{fc.BLACK}Enter the room? (y/n){fc.RESET} ")
                dec = dec.lower()
                acceptable = ['y','n']
                while dec not in acceptable:
                    dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Enter the room? (y/n){fc.RESET} ")
                    dec = dec.lower()
                if dec == 'y':
                    print(f"\nYou enter {fc.YELLOW}the Eastern room{fc.RESET}.")
                    player.location = 'the Eastern room'
                    key_check()
                    if key_check == True:
                        seven_keys = True
                    idlechoice()
                elif dec == 'n':
                    print(f"\nYou have decided to remain in {fc.YELLOW}the Entrance{fc.RESET}.")
                    idlechoice()
            elif unlock == '1' and "Poseidon Key" not in player.inventory:
                print(f"\nYou try to unlock the door, but you don't have the right key for this lock.\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                idlechoice()
            elif unlock == '2':
                player.display_status()                               
            elif unlock == '3':
                print("\nYou have decided not to try the door.")
                idlechoice()
        elif choice == '3' and east_status() == True:
            print(f"\nYou enter the door and return to {fc.YELLOW}the Eastern room{fc.RESET}.")
            player.location = "the Eastern room"
            key_check()
            if key_check == True:
                seven_keys = True
            idlechoice()
    #WESTERN ROOM
    if player.location == "the Western room":
        print(f"\nYou enter the door and return to {fc.YELLOW}the Entrance{fc.RESET}.")
        player.location = "the Entrance"
        idlechoice()
    #NORTHERN ROOM
    if player.location == "the Northern room":
        print(f"\nYou enter the door and return to {fc.YELLOW}the Entrance{fc.RESET}.")
        player.location = "the Entrance"
        idlechoice()
    #EASTERN ROOM
    if player.location == "the Eastern room":
        print(f"\nYou enter the door and return to {fc.YELLOW}the Entrance{fc.RESET}.")
        player.location = "the Entrance"
        idlechoice()


#Search current room function
def roomscan():
    #ENTRANCE
    if player.location == "the Entrance":
        print(f"\nYou take a look around {fc.YELLOW}the Entrance{fc.RESET}.\nYou notice a rug with a strange pattern at its center beneath your feet.\nDirectly above the rug is a {fc.YELLOW}golden{fc.RESET} chandelier with lights that flicker periodically.\nAlong the Western wall, you notice a door. Just to the left of the door is a desk with a lone picture frame sitting on top of it.\nAlong the Northern wall, there is another door with a bookcase sitting just to its right.\nThere is peculiar wooden artwork resembling a famous piece to the right of the door on the Eastern wall.")
        choice = input(f"\n\n{fc.BLACK}Which object would you like to take a closer look at? (1:Rug  2:Chandelier  3:Desk  4:Bookcase  5:Artwork  6:Try a door){fc.RESET} ")
        acceptable = ['1','2','3','4','5','6']
        while choice not in acceptable:
            choice = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which object would you like to take a closer look at? (1:Rug  2:Chandelier  3:Desk  4:Bookcase  5:Artwork  6:Try a door){fc.RESET} ")
        if choice in acceptable:
            if choice == '1':
                rugcheck()
            elif choice == '2':
                chandeliercheck()
            elif choice == '3':
                deskcheck()
            elif choice == '4':
                bookcasecheck()
            elif choice == '5':
                artworkcheck()
            elif choice =='6':
                changerooms()
    #WESTERN ROOM
    elif player.location == "the Western room":
        dec = input(f"\nYou are in {fc.YELLOW}the Western room{fc.RESET}.\nThis room is much smaller than {fc.YELLOW}the Entrance{fc.RESET}.\nIt's a pretty cramped bedroom.\nThere is only a bed, an end table, and a small shelving unit in this room.\n\n{fc.BLACK}Which one would you like to inspect? (1:Bed  2:End table  3:Shelving unit  4:Return to entrance){fc.RESET} ")
        acceptable = ['1','2','3','4']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which one would you like to inspect? (1:Bed  2:End table  3:Shelving unit  4:Return to entrance){fc.RESET} ")
        if dec == '1':
            serrated_knife()
            idlechoice()
        elif dec == '2':
            end_table()
            idlechoice()
        elif dec == '3':
            shelving_unit()
            idlechoice()
        elif dec == '4':
            changerooms()
    #NORTHERN ROOM
    elif player.location == "the Northern room":
        dec = input(f"\nYou are in {fc.YELLOW}the Northern room{fc.RESET}.\nThere is a refrigerator along the left wall, a table with a single chair off to the right, and four podiums line up along the wall in front of you.\n\n{fc.BLACK}Which one would you like to inspect? (1:Fridge  2:Table and chair  3:Podiums  4:Check status  5:Return to entrance){fc.RESET} ")
        acceptable = ['1','2','3','4','5']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which one would you like to inspect? (1:Fridge  2:Table and chair  3:Podiums  4:Check status  5:Return to entrance){fc.RESET} ")
        if dec == '1':
            fridgecheck()
            idlechoice()
        elif dec == '2':
            tablechaircheck()
            idlechoice()
        elif dec == '3':
            podiumcheck()
            idlechoice()
        elif dec == '4':
            player.display_status()
        elif dec == '5':
            changerooms()
    #EASTERN ROOM
    elif player.location == "the Eastern room":
        if 'Slingshot' not in player.inventory:
            dec = input(f"\nYou are in {fc.YELLOW}the Eastern room{fc.RESET}.\nThis room is so tiny that you could only assume it was once a supply closet.\nIt has a {fc.YELLOW}golden{fc.RESET} podium at its center with a lock box resting on it, and an object sitting in the corner on the floor.\n\n{fc.BLACK}Which one would you like to inspect? (1:Golden podium  2:Object  3:Check status  4:Return to entrance){fc.RESET} ")
            acceptable = ['1','2','3','4']
            while dec not in acceptable:
                dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which one would you like to inspect? (1:Golden podium  2:Object  3:Check status  4:Return to entrance){fc.RESET} ")
            if dec == '1':
                goldenpodium()
                idlechoice()
            elif dec == '2':
                slingshot()
                idlechoice()
            elif dec == '3':
                player.display_status()
            elif dec == '4':
                changerooms()
        elif 'Slingshot' in player.inventory:
            dec = input(f"\nYou are in {fc.YELLOW}the Eastern room{fc.RESET}.\nThis room is so tiny that you could only assume it was once a supply closet.\nIt has a {fc.YELLOW}golden{fc.RESET} podium at its center with a lock box resting on it.\n\n{fc.BLACK}What would you like to do? (1:Approach golden podium  2:Check status  3:Return to entrance){fc.RESET} ")
            acceptable = ['1','2','3']
            while dec not in acceptable:
                dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which one would you like to inspect? (1:Golden podium  2:Object  3:Check status  4:Return to entrance){fc.RESET} ")
            if dec == '1':
                goldenpodium()
                idlechoice()
            elif dec == '2':
                player.display_status()
            elif dec == '3':
                changerooms()


#Inspecting the rug
def rugcheck():
    global rug_visited
    global hatch_revealed
    global fridge_looted
    if rug_visited == False:
        rug_visited = True
        dec = input(f"\nUpon closer inspection of the rug, you notice that there is one playing card suit in each corner.\nThe strange pattern at the center looks like a misshapen storm cloud.\n\n{fc.MAGENTA}It might be someone's honest attempt at morphing the four suits into one...{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Move the rug  2:Use an item  3:Never mind){fc.RESET} ")
        acceptable = ['1','2','3']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Move the rug  2:Use an item  3:Never mind){fc.RESET} ")
        if dec == '1':
            print(f"\n\n{fc.RED}The rug is too heavy to move. It must be bolted in place.{fc.RESET}")
            rugcheck()
        elif dec == '2' and "Serrated Knife" not in player.inventory:
            print(f"\n{fc.RED}You have nothing that could be of use here at this time.{fc.RESET}\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            idlechoice()
        elif dec == '2' and "Serrated Knife" in player.inventory and hatch_revealed == False:
            useitem = input(f"\nThe {fc.CYAN}Serrated Knife{fc.RESET} you found earlier looks like it could be used here.\n\n{fc.BLACK}Would you like to use it? (y/n){fc.RESET} ")
            acceptable = ['y','n']
            while useitem not in acceptable:
                useitem = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Would you like to use the {fc.CYAN}Serrated Knife{fc.RESET} here? (y/n){fc.RESET} ")
            if useitem == 'y' and 'unshackled' in player.status:
                hatch_revealed = True
                unlock = input(f"\n\nYou reach into your backpack and pull out the {fc.CYAN}Serrated Knife{fc.RESET}.\nYou cut around the bizarre central design of the rug.\nYou remove the central design to discover a hatch hidden underneath the rug!\nIt has 4 locks, each designed after its own suit.\n\n{fc.BLACK}What would you like to do? (1:Attempt to unlock  2:Eat a snack, then unlock  3:Check status  4:Never mind){fc.RESET} ")
                acceptable = ['1','2','3','4']                
                while unlock not in acceptable:
                    unlock = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Attempt to unlock  2:Eat a snack, then unlock  3:Check status  4:Never mind){fc.RESET} ")
                if unlock == '1':
                    hatch_unlock()
                elif unlock == '2' and fridge_looted == True:
                    print(f"\nYou decide to have a snack before you continue.\nYou eat the food that you found in the fridge earlier.\n\n{fc.MAGENTA}Delicious!{fc.RESET}\n\n{fc.GREEN}(HP fully restored!){fc.RESET}"); player.damage(-100)
                    hatch_unlock()
                elif unlock == '2' and fridge_looted == False:
                    dec = (f"\n\n{fc.RED}You have nothing to snack on!{fc.RESET}\n\n{fc.BLACK}Proceed regardless? (y/n){fc.RESET} ")
                    acceptable = ['y','n']
                    while dec not in acceptable:
                        dec = input(f"\n\n{fc.RED}Make up your mind... enter a valid input...{fc.RESET}")
                    if dec == 'y':
                        hatch_unlock()
                    elif dec == 'n':
                        print(f"\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                        idlechoice()
                elif unlock == '3':
                    player.display_status()
                elif unlock == '4':
                    print(f"\n\nYou have decided to remain in {fc.YELLOW}the Entrance.{fc.RESET}")
                    idlechoice()
            elif useitem == 'y' and hatch_revealed == True:
                hatch_unlock()
            elif useitem == 'y' and 'unshackled' not in player.status and hatch_revealed == False:
                print(f"\n\n{fc.RED}Your handcuffs restrict your movement, you cannot properly cut the rug.{fc.RESET}\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                idlechoice()
        elif dec == '2' and 'Serrated Knife' in player.inventory and all_keys == False:
            useitem = input(f"\nThe {fc.CYAN}Serrated Knife{fc.RESET} you found earlier looks like it could be used here.\n\n{fc.BLACK}Would you like to use it? (y/n){fc.RESET} ")
            acceptable = ['y','n']
            while useitem not in acceptable:
                useitem = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Would you like to use the {fc.CYAN}Serrated Knife{fc.RESET}? (y/n){fc.RESET} ")
            print(f"\nYou do not have the proper keys to unlock the hatch.\n\n{fc.YELLOW}You need to come back later.{fc.RESET}")
            idlechoice()
        elif dec == '3':
            print(f"\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            idlechoice()
    elif rug_visited == True:
        dec = input(f"\nYou are at the rug.\n\n{fc.BLACK}What would you like to do? (1:Move the rug  2:Use an item  3:Never mind){fc.RESET} ")
        acceptable = ['1','2','3']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Move the rug  2:Use an item  3:Never mind){fc.RESET} ")
        if dec == '1':
            print(f"\n\n{fc.RED}The rug is too heavy to move. It must be bolted in place.{fc.RESET}")
            rugcheck()
        elif dec == '2':
            if "Serrated Knife" not in player.inventory:
                print(f"\n{fc.RED}You have nothing that could be of use here at this time.{fc.RESET}\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                idlechoice()
            elif "Serrated Knife" in player.inventory and all_keys == True:
                useitem = input(f"\nThe {fc.CYAN}Serrated Knife{fc.RESET} you found earlier looks like it could be used here.\n\n{fc.BLACK}Would you like to use it? (y/n){fc.RESET} ")
                acceptable = ['y','n']
                while useitem not in acceptable:
                    useitem = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Would you like to use the {fc.CYAN}Serrated Knife{fc.RESET} here? (y/n){fc.RESET} ")
                if useitem == 'y' and 'unshackled' in player.status:
                    unlock = input(f"\n\nYou reach into your backpack and pull out the {fc.CYAN}Serrated Knife{fc.RESET}.\nYou cut around the bizarre central design of the rug.\nYou remove the central design to discover a hatch hidden underneath the rug!\nIt has 4 locks, each designed after its own suit.\n\n{fc.BLACK}What would you like to do? (1:Attempt to unlock  2:Eat a snack, then unlock  3:Check status  4:Never mind){fc.RESET} ")
                    acceptable = ['1','2','3','4']                
                    while unlock not in acceptable:
                        unlock = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Attempt to unlock  2:Check status  3:Check inventory  4:Use consumable item  5:Never mind){fc.RESET} ")
                    if unlock == '1':
                        print(f"\nReacting to the power of the {fc.BLACK}{st.BRIGHT}mind{fc.RESET}{st.NORMAL}, {fc.YELLOW}body{fc.RESET}, {fc.RED}heart{fc.RESET}, and {fc.MAGENTA}soul{fc.RESET}, the door slowly opens.\n\n{fc.GREEN}You have successfully unlocked the hatch!{fc.RESET}\nYou slowly peek your head inside.\nYou can hardly believe your eyes.\nAt the end of a short tunnel, you see what appears to be a parking garage.\nYou climb down the hatch and run straight for the parking garage.\nYou find an unattended police cruiser with the keys sitting in the driver-side door.\nYou can't believe your luck.\nYou unlock the door, climb in the car, buckle up, and start the engine. The engine purs.\nYou yell out in excitement, then let out a massive sigh of relief.\nYou pull out of the parking spot, and head for the exit... ")
                        hatch_unlock()
                    elif unlock == '2' and fridge_looted == True:
                        print(f"\nYou decide to have a snack before you continue.\nYou eat the food that you found in the fridge earlier.\n\n{fc.MAGENTA}Delicious!{fc.RESET}\n\n{fc.GREEN}(HP fully restored!){fc.RESET}"); player.damage(-100)
                        hatch_unlock()
                    elif unlock == '2' and fridge_looted == False:
                        dec = (f"\n\n{fc.RED}You have nothing to snack on!{fc.RESET}\n\n{fc.BLACK}Proceed regardless? (y/n){fc.RESET} ")
                        acceptable = ['y','n']
                        while dec not in acceptable:
                            dec = input(f"\n\n{fc.RED}Make up your mind... enter a valid input...{fc.RESET}")
                        if dec == 'y':
                            hatch_unlock()
                        elif dec == 'n':
                            print(f"\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                            idlechoice()
                    elif unlock == '3':
                        player.display_status()
                    elif unlock == '4':
                        print(f"\n\nYou have decided to remain in {fc.YELLOW}the Entrance.{fc.RESET}")
                        idlechoice()
                elif useitem == 'y' and 'unshackled' not in player.status:
                    print(f"\n\n{fc.RED}Your handcuffs restrict your movement, you cannot properly cut the rug.{fc.RESET}\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                    idlechoice()
            elif 'Serrated Knife' in player.inventory and all_keys == False:
                useitem = input(f"\nThe {fc.CYAN}Serrated Knife{fc.RESET} you found earlier looks like it could be used here.\n\n{fc.BLACK}Would you like to use it? (y/n){fc.RESET} ")
                acceptable = ['y','n']
                while useitem not in acceptable:
                    useitem = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Would you like to use the {fc.CYAN}Serrated Knife{fc.RESET}? (y/n){fc.RESET} ")
                print(f"\nYou do not have the proper keys to unlock the hatch.\n\n{fc.YELLOW}You need to come back later.{fc.RESET}")
                idlechoice()
        elif dec == '3':
            print(f"\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            idlechoice()

#Inspecting the Chandelier
def chandeliercheck():
    if 'Club Key' not in player.inventory:
        dec = input(f"\nYou look up at the chandelier.\nIt looks to be made of solid gold.\nThere are 6 lightbulbs attached to it, 3 of which are flickering, 2 of which are on, and 1 seems... off.\n\n{fc.BLACK}What would you like to do? (1:Inspect further  2:Check status  3:Never mind){fc.RESET} ")
        acceptable = ['1','2','3']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Inspect further  2:Check status  3:Never mind){fc.RESET} ")
        if dec == '1':
            print(f"\nUpon closer inspection, you notice that one of the lightbulbs... is no lightbulb at all!\nIt looks like a container with something inside...\n\nYou're sure that if you can hit it with {fc.CYAN}something{fc.RESET}, it'll get knocked loose and fall to the ground.")
            if "Slingshot" not in player.inventory:
                print(f"\n\nSince you have nothing to hit it with at the moment, {fc.YELLOW}you decide to come back later{fc.RESET}.")
                idlechoice()
            elif "Slingshot" in player.inventory:
                useitem = input(f"\n\n{fc.BLACK}What would you like to do? (1:Use item  2:Never mind){fc.RESET} ")
                acceptable = ['1','2']
                while useitem not in acceptable:
                    useitem = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Use item  2:Never mind){fc.RESET} ")
                if useitem == '1':
                    club_key()
                    idlechoice()
                if useitem == '2':
                    print(f"\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                    idlechoice()
        elif dec == '2':
            player.display_status()
        elif dec == '3':
            print(f"\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            idlechoice()
    elif 'Club Key' in player.inventory:
        club_key()
        idlechoice()


#Inspecting the Desk
def deskcheck():
    global desk_drawer_looted
    global desk_drawer_unlocked
    global desk_approached
    if desk_approached == False:
        desk_approached = True
        dec = input(f"\nYou approach the desk to find a lone framed photograph resting on top.\nYou also notice that there are 3 drawers on the front side of the desk.\n\n{fc.BLACK}What would you like to do? (1:Inspect photo  2:Open left drawer  3:Open middle drawer  4:Open right drawer  5:Never mind){fc.RESET} ")
        acceptable = ['1','2','3','4','5']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Inspect photo  2:Open left drawer  3:Open middle drawer  4:Open right drawer  5:Never mind){fc.RESET} ")
        if dec == '1' and 'Diary Page' not in player.inventory:
            print("\nA photo of a beautiful woman.\nThe back of the frame is a bit sticky.\nYou turn the frame over and see nothing...\n...but after carefully running your hand along the seam near the pins at the top, you feel some tape residue.\nYou hurriedly move the pins aside and open the back of the frame.\nYou find a folded page taped to the back of the photo.")
            diary_page()
            deskcheck()
        elif dec == '1' and 'Diary Page' in player.inventory:
            print("\nThe woman looks just as beautiful as she did before.")
            deskcheck()
        elif dec == '2' and desk_drawer_unlocked == False and 'Square Key' not in player.inventory:
            print(f"\n{fc.RED}This drawer is locked.{fc.RESET}\nIt looks like it could use some sort of key.\nThe lock is {fc.MAGENTA}square{fc.RESET}-shaped.")
            deskcheck()
        elif dec == '2' and desk_drawer_unlocked == False and 'Square Key' in player.inventory:
            desk_drawer_unlocked = True
            print(f"\nThis drawer is locked, but not for long.\n{fc.GREEN}You unlock the drawer with the Square Key!{fc.RESET}")
            artwork_slab()
            deskcheck()
        elif dec == '2' and desk_drawer_unlocked == True:
            artwork_slab()
            deskcheck()
        elif dec == '3' and desk_drawer_looted == False:
            desk_drawer_looted = True
            print(f"\n{fc.GREEN}You open the middle drawer to find some medical supplies!{fc.RESET}")
            player.add_inventory_item('Painkillers')
            player.add_inventory_item('Peroxide')
            player.add_inventory_item('Bandage')
            player.add_inventory_item('Bandage')
            print(f"\nYou take all of the painkillers, splash your leg with peroxide, and use the bandages to cover your wound.\n\n{fc.GREEN}(HP fully restored!){fc.RESET} "); player.damage(-100)
            deskcheck()
        elif dec == '3' and desk_drawer_looted == True:
            print(f"\n{fc.RED}You have already looted this drawer for all of its contents.{fc.RESET}")
            deskcheck()
        elif dec == '4':
            print(f"\n{fc.RED}You don't find anything of use in this drawer.{fc.RESET}")
            deskcheck()
        elif dec == '5':
            print(f"\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            idlechoice()
    elif desk_approached == True:
        dec = input(f"\nYou are at the desk.\n\n{fc.BLACK}What would you like to do? (1:Inspect photo  2:Open left drawer  3:Open middle drawer  4:Open right drawer  5:Never mind){fc.RESET} ")
        acceptable = ['1','2','3','4','5']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Inspect photo  2:Open left drawer  3:Open middle drawer  4:Open right drawer  5:Never mind){fc.RESET} ")
        if dec == '1' and 'Diary Page' not in player.inventory:
            print("\nA photo of a beautiful woman.\nThe back of the frame is a bit sticky.\nYou turn the frame over and see nothing...\n...but after carefully running your hand along the seam near the pins at the top, you feel some tape residue.\nYou hurriedly move the pins aside and open the back of the frame.\nYou find a folded page taped to the back of the photo.")
            diary_page()
            deskcheck()
        elif dec == '1' and 'Diary Page' in player.inventory:
            print("\nThe woman looks just as beautiful as she did before.")
            deskcheck()
        elif dec == '2' and desk_drawer_unlocked == False and 'Square Key' not in player.inventory:
            print(f"\n{fc.RED}This drawer is locked.{fc.RESET}\nIt looks like it could use some sort of key.\nThe lock is {fc.MAGENTA}square{fc.RESET}-shaped.")
            deskcheck()
        elif dec == '2' and desk_drawer_unlocked == False and 'Square Key' in player.inventory:
            desk_drawer_unlocked = True
            print(f"\nThis drawer is locked, but not for long.\n{fc.GREEN}You unlock the drawer with the Square Key!{fc.RESET}\nThere is a mysterious slab inside...")
            artwork_slab()
            deskcheck()
        elif dec == '2' and desk_drawer_unlocked == True:
            artwork_slab()
            deskcheck()
        elif dec == '3' and desk_drawer_looted == False:
            desk_drawer_looted = True
            print(f"\n{fc.GREEN}You open the middle drawer to find some medical supplies!{fc.RESET}")
            player.add_inventory_item('Painkillers')
            player.add_inventory_item('Peroxide')
            player.add_inventory_item('Bandage')
            player.add_inventory_item('Bandage')
            print(f"\nYou take all of the painkillers, splash your leg with peroxide, and use the bandages to cover your wound.\n\n{fc.GREEN}(HP fully restored!){fc.RESET} "); player.damage(-100)
            deskcheck()
        elif dec == '3' and desk_drawer_looted == True:
            print(f"\n{fc.RED}You have already looted this drawer for all of its contents.{fc.RESET}")
            deskcheck()
        elif dec == '4':
            print(f"\n{fc.RED}You don't find anything of use in this drawer.{fc.RESET}")
            deskcheck()
        elif dec == '5':
            print(f"\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            idlechoice()


#Inspecting the Bookcase
def bookcasecheck():
    global bookcase_visited
    global bookcase_looted
    global yellow_book_discovered
    if bookcase_visited == False:
        bookcase_visited = True
        dec = input(f"\nYou walk up to a beautiful, towering ivory bookcase that has three shelves full of books.\nThere are many beat-up brown books on these shelves.\n\n{fc.BLACK}What would you like to do? (1:Examine books  2:Examine shelves  3:Check status  4:Never mind){fc.RESET} ")
        acceptable = ['1','2','3','4']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Examine books  2:Examine shelves  3:Check status  4:Never mind){fc.RESET} ")
        if dec == '1':
            yellow_book_discovered = True
            book_dec = input(f"\nYou take a closer look at the beat-up brown books.\nThey are packed tightly against one another across the top two shelves.\nThe bottom shelf, however, has a loose book leaning to its side.\nYou pull that book out to discover a bright {fc.YELLOW}yellow{fc.RESET} book that appears to be in mint condition hidden on its side behind it!\n\n{fc.BLACK}What would you like to do? (1:Inspect further  2:Never mind){fc.RESET} ")
            book_acceptable = ['1','2']
            while book_dec not in book_acceptable:
                book_dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Inspect further  2:Never mind){fc.RESET} ")
            if book_dec == '1' and 'Serrated Knife' not in player.inventory:
                print(f"\nYou grab the yellow book to inspect it closer.\nThe book feels a little heavy, so you open it face down and shake it.\n{fc.GREEN}A small key falls out of the book and onto the floor!{fc.RESET}")
                handcuff_key()
                print(f"\nAs you go to place the book down on the bookcase, you feel a bump in its spine.\nPerhaps if you had {fc.MAGENTA}something sharp{fc.RESET} you could investigate this mysterious bump...\n\n{fc.YELLOW}You place the book down on the bookcase and decide to come back later.{fc.RESET}")
                idlechoice()
            elif book_dec == '1' and 'Serrated Knife' in player.inventory:
                print(f"\nYou grab the yellow book to inspect it closer.\nThe book feels a little heavy, so you open it face down and shake it.\n{fc.GREEN}A small key falls out of the book and onto the floor!{fc.RESET}")
                handcuff_key()
                print(f"\nAs you go to place the book down on the bookcase, you feel a bump in its spine.")
                cross_key()
                idlechoice()
            elif book_dec == '2':
                print(f"\n{fc.YELLOW}You decide to leave the yellow book alone for now, but take note of its existence as you walk away.{fc.RESET}")
                idlechoice()
        elif dec == '2' and bookcase_looted == False:
            bookcase_looted = True
            print(f"\nYou peek at the first and second shelves, but find nothing.\nYou reach your hands onto the third shelf, running it across from one end to the other, when you feel something with your fingertips.")
            square_key()
            idlechoice()
        elif dec == '2' and bookcase_looted == True:
            square_key()
            idlechoice()
        elif dec == '3':
            player.display_status()
        elif dec == '4':
            print(f"\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            idlechoice()
    elif bookcase_visited == True:
        dec = input(f"\nYou walk back up to the bookcase.\n\n{fc.BLACK}What would you like to do? (1:Examine yellow book  2:Examine shelves  3:Check status  4:Never mind){fc.RESET} ")
        acceptable = ['1','2','3','4']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Examine books  2:Examine shelves  3:Check status  4:Never mind){fc.RESET} ")
        if dec == '1' and yellow_book_discovered == False:
            yellow_book_discovered = True
            book_dec = input(f"\nYou take a closer look at the beat-up brown books.\nThey are packed tightly against one another across the top two shelves.\nThe bottom shelf, however, has a loose book leaning to its side.\nYou pull that book out to discover a bright {fc.YELLOW}yellow{fc.RESET} book that appears to be in mint condition hidden on its side behind it!\n\n{fc.BLACK}What would you like to do? (1:Inspect further  2:Never mind){fc.RESET} ")
            book_acceptable = ['1','2']
            while book_dec not in book_acceptable:
                book_dec = input(f"\n\n{fc.BLACK}What would you like to do? (1:Inspect further  2:Never mind){fc.RESET} ")
            if book_dec == '1' and 'Serrated Knife' not in player.inventory:
                print(f"\nYou grab the yellow book to inspect it closer.\nThe book feels a little heavy, so you open it face down and shake it.\n{fc.GREEN}A small key falls out of the book and onto the floor!{fc.RESET}")
                handcuff_key()
                print(f"\nAs you go to place the book down on the bookcase, you feel a bump in its spine.\nPerhaps if you had {fc.MAGENTA}something sharp{fc.RESET} you could investigate this mysterious bump...\n\n{fc.YELLOW}You place the book down on the bookcase and decide to come back later.{fc.RESET}")
                idlechoice()
            elif book_dec == '1' and 'Serrated Knife' in player.inventory:
                print(f"\nYou grab the yellow book to inspect it closer.\nThe book feels a little heavy, so you open it face down and shake it.\n{fc.GREEN}A small key falls out of the book and onto the floor!{fc.RESET}")
                handcuff_key()
                print(f"\nAs you go to place the book down on the bookcase, you feel a bump in its spine.")
                cross_key()
                idlechoice()
            elif book_dec == '2':
                print(f"\n{fc.YELLOW}You decide to leave the yellow book alone for now, but take note of its existence as you walk away.{fc.RESET}")
                idlechoice()    
        elif dec == '1' and yellow_book_discovered == True and 'Handcuff Key' not in player.inventory:
            book_dec = input(f"\nYou take a closer look at the beat-up brown books.\nThey are packed tightly against one another across the top two shelves.\nThe bottom shelf, however, has a loose book leaning to its side.\nYou pull that book out to discover a bright {fc.YELLOW}yellow{fc.RESET} book that appears to be in mint condition hidden on its side behind it!\n\n{fc.BLACK}What would you like to do? (1:Inspect further  2:Never mind){fc.RESET} ")
            book_acceptable = ['1','2']
            while book_dec not in book_acceptable:
                book_dec = input(f"\n\n{fc.BLACK}What would you like to do? (1:Inspect further  2:Never mind){fc.RESET} ")
            if book_dec == '1' and 'Serrated Knife' not in player.inventory:
                print(f"\nYou grab the yellow book to inspect it closer.\nThe book feels a little heavy, so you open it face down and shake it.\n{fc.GREEN}A small key falls out of the book and onto the floor!{fc.RESET}")
                handcuff_key()
                print(f"\nAs you go to place the book down on the bookcase, you feel a bump in its spine.\nPerhaps if you had {fc.MAGENTA}something sharp{fc.RESET} you could investigate this mysterious bump...\n\n{fc.YELLOW}You place the book down on the bookcase and decide to come back later.{fc.RESET}")
                idlechoice()
            elif book_dec == '1' and 'Serrated Knife' in player.inventory:
                print(f"\nYou grab the yellow book to inspect it closer.\nThe book feels a little heavy, so you open it face down and shake it.\n{fc.GREEN}A small key falls out of the book and onto the floor!{fc.RESET}")
                handcuff_key()
                print(f"\nAs you go to place the book down on the bookcase, you feel a bump in its spine.")
                cross_key()
                idlechoice()
            elif book_dec == '2':
                print(f"\n{fc.YELLOW}You decide to leave the yellow book alone for now, but take note of its existence as you walk away.{fc.RESET}")
                idlechoice()
        elif dec == '1' and 'Serrated Knife' not in player.inventory and 'Handcuff Key' in player.inventory:
            print(f"\nYou are still missing something sharp to cut open the spine of the book.\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            idlechoice()
        elif dec == '1' and 'Serrated Knife' in player.inventory and 'Handcuff Key' in player.inventory and 'Cross Key' not in player.inventory:
            cross_key()
            idlechoice()
        elif dec == '1' and 'Cross Key' and 'Handcuff Key' in player.inventory:
            handcuff_key()
            cross_key()
            idlechoice()
        elif dec == '2' and bookcase_looted == False:
            bookcase_looted = True
            print(f"\nYou peek at the first and second shelves, but find nothing.\nYou reach your hands onto the third shelf, running it across from one end to the other, when you feel something with your fingertips.")
            square_key()
            idlechoice()
        elif dec == '2' and bookcase_looted == True:
            square_key()
            idlechoice()
        elif dec == '3':
            player.display_status()
        elif dec == '4':
            print(f"\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            idlechoice()


#Inspecting the Artwork
def artworkcheck():
    global artwork_visited
    global slab_placed
    if artwork_visited == False and 'Artwork Slab' not in player.inventory:
        artwork_visited = True
        print(f"\nYou approach the wooden artwork and immediately recognize it as the Vitruvian Man, but something seems... off.\nThere is a very specific... section... missing.\nPerhaps you can find the missing wood elsewhere.")
        idlechoice()
    elif artwork_visited == False and 'Artwork Slab' in player.inventory:
        artwork_visited = True
        slab_placed = True
        print(f"\nYou approach the wooden artwork and immediately recognize it as the Vitruvian Man, but something seems... off.\nThere is a very specific... section... missing.\nYou realize that the slab of wood that you grabbed earlier should slot perfectly into place here.\n\n...\n\nIt was a tight fit, but the wooden slab has been returned to its rightful place.\n\n{fc.GREEN}You hear a distinct clicking sound!{fc.RESET}")
        west_status()
        idlechoice()
    elif artwork_visited == True and slab_placed == False and 'Artwork Slab' not in player.inventory:
        print(f"\nThe Vitruvian Man, without a shred of dignity.\n{fc.YELLOW}You decide to come back once you have found a way to help this... unfortunate man.{fc.RESET}")
        idlechoice()
    elif artwork_visited == True and slab_placed == False and 'Artwork Slab' in player.inventory:
        slab_placed = True
        print(f"\nThe Vitruvian Man, without a shred of dignity.\nYou realize that the slab of wood that you grabbed earlier should slot perfectly into place here.\n\n...\n\nIt was a tight fit, but the wooden slab has been returned to its rightful place.\n\n{fc.GREEN}You hear a distinct clicking sound!{fc.RESET}")
        west_status()
        idlechoice()       
    elif slab_placed == True:
        print(f"\nThe Vitruvian Man, restored to his former glory.\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")
        idlechoice()


#Inspecting the End Table
def end_table():
    global end_table_visited
    global end_bottom_visited
    if end_table_visited == False:
        end_table_visited = True
        print(f"\nYou move towards the end table and stub your toe very hard on the end of the bed. Ouch! {fc.RED}(-20 HP){fc.RESET}"); player.damage(20)
        dec = input(f"\nOnce in front of the end table, you notice that there are 2 drawers.\n\n{fc.BLACK}What would you like to do? (1:Open top drawer  2:Open bottom drawer  3:Never mind){fc.RESET} ")
        acceptable = ['1','2','3']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Open top drawer  2:Open bottom drawer  3:Never mind){fc.RESET} ")
        if dec == '1':
            triangle_and_diamond_key()
            end_table()
        elif dec =='2':
            end_table_bottom()
            end_bottom_visited = True
            end_table()
        elif dec == '3':
            print("\nYou step away from the end table.")
            idlechoice()
    elif end_table_visited ==True:
        dec = input(f"\nYou are at the end table.\n\n{fc.BLACK}What would you like to do? (1:Open top drawer  2:Open bottom drawer  3:Never mind){fc.RESET} ")
        acceptable = ['1','2','3']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Open top drawer  2:Open bottom drawer  3:Never mind){fc.RESET} ")
        if dec == '1':
            triangle_and_diamond_key()
            end_table()
        elif dec == '2':
            end_table_bottom()
            end_bottom_visited = True
            end_table()
        elif dec == '3':
            print(f"\nYou step away from the end table.")
            idlechoice()

def end_table_bottom():
    global end_bottom_visited
    if end_bottom_visited == False:
        print(f"\nYou open the bottom drawer.\n{fc.GREEN}You find a ton of healing items inside!{fc.RESET}")
        player.add_inventory_item('Bandage')
        player.add_inventory_item('Painkillers')
        player.add_inventory_item('Peroxide')
        player.add_inventory_item('Antidote')
        player.add_inventory_item('Snack Bar')
    elif end_bottom_visited == True:
        print(f"\n{fc.RED}You have already looted this drawer for all of its contents.{fc.RESET}")


#Inspecting the Shelving Unit
def shelving_unit():
    dec = input(f"\nYou approach the shelving unit.\nThis unit has only 2 shelves.\n\n{fc.BLACK}Which shelf would you like to check? (1:Top shelf  2:Bottom shelf){fc.RESET} ")
    acceptable = ['1','2']
    while dec not in acceptable:
        dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which shelf would you like to check? (1:Top shelf  2:Bottom shelf){fc.RESET} ")
    if dec == '1':
        circle_key()
        idlechoice()
    elif dec == '2':
        boltcutters()
        idlechoice()


#Inspecting the Fridge
def fridgecheck():
    global fridge_looted
    dec = input(f"\nYou approach the refrigerator.\n\n{fc.BLACK}What would you like to do? (1:Open fridge  2:Never mind){fc.RESET} ")
    acceptable = ['1','2']
    while dec not in acceptable:
        dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Open fridge  2:Never mind){fc.RESET} ")    
    if dec == '1' and fridge_looted == False:
        dec = input(f"\nThe fridge door is stuck.\n\n{fc.BLACK}What would you like to do? (1:OPEN FRIDGE  2:Never mind){fc.RESET} ")
        acceptable = ['1','2']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:OPEN FRIDGE  2:Never mind){fc.RESET} ")  
        if dec == '1':
            dec = input(f"\nThe fridge door is STILL stuck.\n\n{fc.BLACK}What would you like to do? (1:OPEN. THE. FRIDGE.){fc.RESET} ")
            acceptable = ['1']
            while dec not in acceptable:
                dec = input(f"\n\n{fc.RED}Seriously? There is only one input option here...{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:OPEN. THE. FRIDGE.){fc.RESET} ")
            if dec == '1':
                fridge_looted = True
                print(f"\n\n{fc.GREEN}You successfully win your unnecessarily long battle with the fridge!{fc.RESET}\nThere are many goodies inside, and you take them all.")
                player.add_inventory_item('Banana')
                player.add_inventory_item('Banana')
                player.add_inventory_item('Apple')
                player.add_inventory_item('Orange')
                player.add_inventory_item('Bottle of water')
                player.add_inventory_item('Bottle of water')
                idlechoice()
        elif dec == '2':
            print(f"\n\n{fc.YELLOW}You give up and walk away.{fc.RESET}\n\n{fc.MAGENTA}It's a good thing nobody's around to have witnessed you backing down from a simple fridge... that would be embarrassing.{fc.RESET}")
            idlechoice()
    elif dec == '1' and fridge_looted == True:
        print(f"\nYou remember your massive victory over this fridge.\n\n{fc.YELLOW}You stand proud.{fc.RESET}")
        idlechoice()
    elif dec == '2':
        print(f"\nSomething about this fridge really intimidates you.\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
        idlechoice()

#Inspecting the Table and Chair
def tablechaircheck():
    global chair_broken
    if chair_broken == False:
        dec = input(f"\nIt's a simple table with nothing on it and a lone chair beside it.\n\n{fc.BLACK}Would you like to rest in the chair? (y/n){fc.RESET} ")
        acceptable = ['y','n']
        while dec not in acceptable:
            dec = input(f"\n\n{fc.RED}It's a simple question, really.{fc.RESET}\n\n{fc.BLACK}Would you like to rest in the chair? (y/n){fc.RESET}")
        if dec == 'y' and player.health <= 50:
            print(f"\nYou decide to take a load off for a moment. {fc.GREEN}(+25 HP)"); player.damage(-25)
            idlechoice()
        elif dec == 'y' and player.health > 50:
            print(f"\nYou decide to take a load off for a moment. {fc.GREEN}(+25 HP)"); player.damage(-25)
            print(f"\n\n{fc.RED}The chair broke!{fc.RESET} ")
            chair_broken = True
            idlechoice()
    elif chair_broken == True:
        print(f"\nYou abused the poor chair too much...\n{fc.YELLOW}There is nothing left of importance here.{fc.RESET}")
        idlechoice()

#Inspecting the Podiums
def podiumcheck():
    global loose_brick
    global square_puzzle
    global circle_puzzle
    global triangle_puzzle
    global cross_puzzle
    global podiums_visited
    if loose_brick == True:
        poseidon_key()
        idlechoice()
    elif podiums_visited == False:
        podiums_visited = True
        dec = input(f"\nYou approach the four podiums.\nEach one has a design based on four familiar shapes - a {fc.MAGENTA}square{fc.RESET}, a {fc.RED}circle{fc.RESET}, a {fc.GREEN}triangle{fc.RESET}, and a {fc.BLUE}cross{fc.RESET}.\nThe podiums are laid out as if they were made to work a station for playing.\n\n{fc.BLACK}Which podium would you like to inspect? (1:Square  2:Circle  3:Triangle  4:Cross  5:Never mind){fc.RESET} ")
        acceptable = ['1','2','3','4','5']
        while dec not in acceptable:
            dec = input (f"\n\n{fc.RED}Please enter a valid input.\n\n{fc.BLACK}Which podium would you like to inspect? (1:Square  2:Circle  3:Triangle  4:Cross  5:Never mind){fc.RESET} ")
        if dec == '1' and square_puzzle == False:
            choice = input(f"\nThere is a keyboard and a small screen resting on this podium.\nThe screen reads:\n\nEnter the day that the {fc.MAGENTA}beauty{fc.RESET} discovered how to escape from the {fc.RED}Devil{fc.RESET}.\n\n{fc.YELLOW}(Ex. January 1, 1900){fc.RESET} \n\n{fc.BLACK}What would you like to do? (1:Enter code  2:Check inventory){fc.RESET} ")
            accept = ['1','2']
            while choice not in accept:
                choice = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Enter code  2:Check inventory) ")
            while choice == '2' and 'Diary Page' in player.inventory:
                inspect_page()
                choice = '1'
            while choice == '2' and 'Diary Page' not in player.inventory:
                print(f"\n\n{fc.RED}You don't have anything in your inventory that could be of assistance here.{fc.RESET}")
                choice = '1'
            if choice == '1':
                code = input(f"\n\n{fc.YELLOW}(Ex. January 1, 1900){fc.RESET}\n\n{fc.BLACK}Enter code: {fc.RESET}")
                solution = 'February 15, 1989'
                if code != solution:
                    print(f"\n\n{fc.RED}Incorrect solution.{fc.RESET}\n\n{fc.MAGENTA}The keyboard shocks you!{fc.RESET} {fc.RED}(-15 HP){fc.RESET}, "); player.damage(15)
                    print(f"\n\n{fc.YELLOW}You decide to catch your breath before trying again.{fc.RESET}")
                    podiumcheck()
                elif code == solution:
                    print(f"\n\n{fc.GREEN}You have entered the correct solution!{fc.RESET}\n\nA slot opens on the front of the podium with a key inside!\n\n{fc.MAGENTA}You also hear a click!{fc.RESET}")
                    square_puzzle = True
                    heart_key()
                    podiumcheck()
        elif dec == '1' and square_puzzle == True:
            heart_key()
            podiumcheck()
        elif dec == '2' and circle_puzzle == False:
            dec = input(f"\nThere is a note and a {fc.BLACK}{st.BRIGHT}black{fc.RESET}{st.NORMAL} potion on this podium.\nThe note reads:\n\n<If one wishes to escape the {fc.RED}Devil{fc.RESET}, one must first learn how to cheat {fc.BLACK}{st.DIM}death{fc.RESET}{st.NORMAL}.>\n\nYou're not sure what it means, but you get the feeling that someone, or something, is waiting for you to drink this potion...\n\n{fc.BLACK}Drink the potion? (y/n){fc.RESET} ")
            acceptable = ['y','n']
            while dec not in acceptable:
                dec = input(f"\n\nThis is a hard decision, but {fc.RED}please enter a valid input{fc.RESET}.\n\n{fc.BLACK}Drink the potion? (y/n){fc.RESET} ")
            if dec == 'y':
                circle_puzzle = True
                print(f"\nYou guzzle down every last drop of the deathly potion.\n\nYou feel {fc.YELLOW}sick{fc.RESET} to your stomach... {fc.RED}(-40 HP){fc.RESET}"); player.damage(40); print(f"\n{fc.MAGENTA}You hear a click.{fc.RESET} ")
                podiumcheck()
            elif dec == 'n':
                print(f"\nYou're not sure what it means, but you choose not to risk it for the moment.\n\n{fc.YELLOW}You decide to come ba---{fc.RESET}\n\n{fc.RED}C O W A R D !{fc.RESET}\n\nA {fc.MAGENTA}small dart{fc.RESET} flies out of the front of the podium at you!\nIt hits you square in the chest. {fc.RED}(-15 HP), "); player.damage(15); print(f"({fc.RED}{player.health}{fc.RESET} HP remaining) ")
                podiumcheck()
        elif dec == '2' and circle_puzzle == True:
            print(f"\n\n{fc.YELLOW}You have already solved this puzzle, there is nothing left for you to do here.{fc.RESET}")
            podiumcheck()
        elif dec == '3' and triangle_puzzle == False and 'Serrated Knife' in player.inventory:
            dec = input(f"\nThere is an engraving on this podium, as well as a red button under a plastic cover that is held closed by a lock.\nNo key you have seen before can remove this lock.\nThe engraving reads:\n\n<The Hero with the {fc.CYAN}broken blade{fc.RESET} must sacrifice more than his {fc.CYAN}weapon{fc.RESET} to escape the {fc.RED}Devil{fc.RESET}.>\n\nYou're not quite sure what it means, but you feel like one of your items can be used here...\n\n{fc.BLACK}Which item would you like to try to use? (1:Damaged Screwdriver  2:Serrated Knife  3:Never mind){fc.RESET} ")
            acceptable = ['1','2','3']
            while dec not in acceptable:
                dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which item would you like to try to use? (1:Damaged Screwdriver  2:Serrated Knife  3:Never mind){fc.RESET} ")
            if dec == '1':
                triangle_puzzle = True
                print(f"\nYou jam your {fc.CYAN}Damaged Screwdriver{fc.RESET} into the lock and begin to twist.\n\n{fc.RED}The screwdriver breaks in half, injuring your hand in the process! (-25 HP){fc.RESET}"); player.damage (25); player.remove_inventory_item('Damaged Screwdriver'); print(f"Your trusty screwdriver falls to the floor...\n\n{fc.GREEN}The lock has been opened!{fc.RESET}\n\n{fc.MAGENTA}You hurriedly push the button, and hear a click.{fc.RESET}")
                podiumcheck()
            elif dec == '2':
                print(f"\nYour {fc.CYAN}Serrated Knife{fc.RESET} does not fit into the lock.\n\n{fc.YELLOW}Perhaps you should try a different item...{fc.RESET}")
                podiumcheck()
            elif dec == '3':
                print(f"\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                idlechoice()
        elif dec == '3' and triangle_puzzle == False and 'Serrated Knife' not in player.inventory:
            dec = input(f"\nThere is an engraving on this podium, as well as a red button under a plastic cover that is held closed by a lock.\nNo key you have seen before can remove this lock.\nThe engraving reads:\n\n<The Hero with the {fc.CYAN}broken blade{fc.RESET} must sacrifice more than his {fc.CYAN}weapon{fc.RESET} to escape the {fc.RED}Devil{fc.RESET}.>\n\nYou're not quite sure what it means, but you feel like one of your items can be used here...\n\n{fc.BLACK}Which item would you like to try to use? (1:Damaged Screwdriver  2:Serrated Knife  3:Never mind){fc.RESET} ")
            acceptable = ['1','2']
            while dec not in acceptable:
                dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which item would you like to try to use? (1:Damaged Screwdriver  2:Serrated Knife  3:Never mind){fc.RESET} ")
            if dec == '1':
                triangle_puzzle = True
                print(f"\nYou jam your {fc.CYAN}Damaged Screwdriver{fc.RESET} into the lock and begin to twist.\n\n{fc.RED}The screwdriver breaks in half, injuring your hand in the process! (-25 HP){fc.RESET}, "); player.damage (25); player.remove_inventory_item('Damaged Screwdriver'); print(f"({fc.RED}{player.health}{fc.RESET} HP remaining)\nYour trusty screwdriver falls to the floor...\n\n{fc.GREEN}The lock has been opened!{fc.RESET}\n\n{fc.MAGENTA}You hurriedly push the button, and hear a click.{fc.RESET}")
                podiumcheck()
            elif dec == '2':
                print(f"\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                idlechoice()
        elif dec == '3' and triangle_puzzle == True:
            print(f"\nThis is where you lost your trusty screwdriver.\n\n{fc.YELLOW}There is nothing left of interest here.{fc.RESET}")
            podiumcheck()
        elif dec == '4' and cross_puzzle == False:
            dec = input(f"\nThis podium has a beautiful velvet cover draped over it with a tag sticking out of the side of the cover.\nThe tag reads:\n\n<The {fc.MAGENTA}teeth{fc.RESET} used to break this lock are the same {fc.MAGENTA}teeth{fc.RESET} that shall reveal this lock.>\n\n{fc.BLACK}What would you like to do? (1:Destroy the beautiful velvet cover  2:Walk away without feeling guilty about destroying something so beautiful){fc.RESET} ")
            acceptable = ['1','2']
            while dec not in acceptable:
                dec = input(f"\n\n{fc.RED}Oh, come on, this one's easy.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Destroy the beautiful velvet cover  2:Walk away without feeling guilty about destroying something so beautiful){fc.RESET} ")                
            if dec == '1' and 'Serrated Knife' in player.inventory:
                cross_puzzle = True
                print(f"\nYou could not care less about someone else's hard work.\nYou pull out your {fc.CYAN}Serrated Knife{fc.RESET} and slash away at the innocent, beautiful velvet cover on the podium.\n\n{fc.GREEN}Congratulations on being a jerk, you found a red button!{fc.RESET}\n\n{fc.MAGENTA}You push the red button and hear a click!{fc.RESET}")
                podiumcheck()
            elif dec == '1' and 'Serrated Knife' not in player.inventory:
                print(f"\nYou could not care less about someone else's hard work, but you do not have an item you could use here.\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            elif dec == '2':
                print(f"\nYou leave the beautiful velvet cover intact. {fc.RED}C O W A R D !{fc.RESET}\nBefore you can react, the velvet cover flies off of the podium and wraps itself around your face.\n\nWhy... do... you... smell... chloroform...? ...\n\n..................\n\nYou come to after a few minutes.\nThe sheer embarrassment of losing to a rug causes you to slap yourself in the face a bit too hard. {fc.RED}(-15 HP){fc.RESET}"); player.damage(15)
                podiumcheck()
        elif dec == '4' and cross_puzzle == True:
            print(f"\n\n{fc.YELLOW}There is nothing left of interest here.{fc.RESET}")
            podiumcheck()
        elif dec == '5':
            print(f"\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
            idlechoice()
    elif podiums_visited == True:
        if square_puzzle == False or circle_puzzle == False or triangle_puzzle == False or cross_puzzle == False:
            dec = input(f"\nYou are at the podiums.\n\n{fc.BLACK}Which podium would you like to inspect? (1:Square  2:Circle  3:Triangle  4:Cross  5:Never mind){fc.RESET} ")
            acceptable = ['1','2','3','4','5']
            while dec not in acceptable:
                dec = input (f"\n\n{fc.RED}Please enter a valid input.\n\n{fc.BLACK}Which podium would you like to inspect? (1:Square  2:Circle  3:Triangle  4:Cross  5:Never mind){fc.RESET} ")
            if dec == '1' and square_puzzle == False:
                choice = input(f"\nThere is a keyboard and a small screen resting on this podium.\nThe screen reads:\n\nEnter the day that the {fc.MAGENTA}beauty{fc.RESET} discovered how to escape from the {fc.RED}Devil{fc.RESET}.\n\n{fc.YELLOW}(Ex. January 1, 1900){fc.RESET} \n\n{fc.BLACK}What would you like to do? (1:Enter code  2:Check inventory){fc.RESET} ")
                accept = ['1','2']
                while choice not in accept:
                    choice = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Enter code  2:Check inventory) ")
                while choice == '2' and 'Diary Page' in player.inventory:
                    inspect_page()
                    choice = '1'
                if choice == '1':
                    code = input(f"\n\n{fc.YELLOW}(Ex. January 1, 1900){fc.RESET}\n\n{fc.BLACK}Enter code: {fc.RESET}")
                    solution = 'February 15, 1989'
                    if code != solution:
                        print(f"\n\n{fc.RED}Incorrect solution.{fc.RESET}\n\n{fc.MAGENTA}The keyboard shocks you!{fc.RESET} {fc.RED}(-15 HP){fc.RESET}, "); player.damage(15)
                        print(f"\n\n{fc.YELLOW}You decide to catch your breath before trying again.{fc.RESET}")
                        podiumcheck()
                    elif code == solution:
                        print(f"\n\n{fc.GREEN}You have entered the correct solution!{fc.RESET}\n\nA slot opens on the front of the podium with a key inside!\n\n{fc.MAGENTA}You also hear a click!{fc.RESET}")
                        square_puzzle = True
                        heart_key()
                        podiumcheck()
            elif dec == '1' and square_puzzle == True:
                heart_key()
                podiumcheck()
            elif dec == '2' and circle_puzzle == False:
                dec = input(f"\nThere is a note and a {fc.BLACK}{st.BRIGHT}black{fc.RESET}{st.NORMAL} potion on this podium.\nThe note reads:\n\n<If one wishes to escape the {fc.RED}Devil{fc.RESET}, one must first learn how to cheat {fc.BLACK}{st.DIM}death{fc.RESET}{st.NORMAL}.>\n\nYou're not sure what it means, but you get the feeling that someone, or something, is waiting for you to drink this potion...\n\n{fc.BLACK}Drink the potion? (y/n){fc.RESET} ")
                acceptable = ['y','n']
                while dec not in acceptable:
                    dec = input(f"\n\nThis is a hard decision, but {fc.RED}please enter a valid input{fc.RESET}.\n\n{fc.BLACK}Drink the potion? (y/n){fc.RESET} ")
                if dec == 'y':
                    circle_puzzle = True
                    print(f"\nYou guzzle down every last drop of the deathly potion.\n\nYou feel {fc.YELLOW}sick{fc.RESET} to your stomach... {fc.RED}(-40 HP){fc.RESET}"); player.damage(40); print(f"\n{fc.MAGENTA}You hear a click.{fc.RESET} ")
                    podiumcheck()
                elif dec == 'n':
                    print(f"\nYou're not sure what it means, but you choose not to risk it for the moment.\n\n{fc.YELLOW}You decide to come ba---{fc.RESET}\n\n{fc.RED}C O W A R D !{fc.RESET}\n\nA {fc.MAGENTA}small dart{fc.RESET} flies out of the front of the podium at you!\nIt hits you square in the chest. {fc.RED}(-15 HP)"); player.damage(15)
                    podiumcheck()
            elif dec == '2' and circle_puzzle == True:
                print(f"\n\n{fc.YELLOW}You have already solved this puzzle, there is nothing left for you to do here.{fc.RESET}")
                podiumcheck()
            elif dec == '3' and triangle_puzzle == False and 'Serrated Knife' in player.inventory:
                dec = input(f"\nThere is an engraving on this podium, as well as a red button under a plastic cover that is held closed by a lock.\nNo key you have seen before can remove this lock.\nThe engraving reads:\n\n<The Hero with the {fc.CYAN}broken blade{fc.RESET} must sacrifice more than his {fc.CYAN}weapon{fc.RESET} to escape the {fc.RED}Devil{fc.RESET}.>\n\nYou're not quite sure what it means, but you feel like one of your items can be used here...\n\n{fc.BLACK}Which item would you like to try to use? (1:Damaged Screwdriver  2:Serrated Knife  3:Never mind){fc.RESET} ")
                acceptable = ['1','2','3']
                while dec not in acceptable:
                    dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which item would you like to try to use? (1:Damaged Screwdriver  2:Serrated Knife  3:Never mind){fc.RESET} ")
                if dec == '1':
                    triangle_puzzle = True
                    print(f"\nYou jam your {fc.CYAN}Damaged Screwdriver{fc.RESET} into the lock and begin to twist.\n\n{fc.RED}The screwdriver breaks in half, injuring your hand in the process! (-25 HP){fc.RESET}"); player.damage (25); player.remove_inventory_item('Damaged Screwdriver'); print(f"Your trusty screwdriver falls to the floor...\n\n{fc.GREEN}The lock has been opened!{fc.RESET}\n\n{fc.MAGENTA}You hurriedly push the button, and hear a click.{fc.RESET}")
                    podiumcheck()
                elif dec == '2':
                    print(f"\nYour {fc.CYAN}Serrated Knife{fc.RESET} does not fit into the lock.\n\n{fc.YELLOW}Perhaps you should try a different item...{fc.RESET}")
                    podiumcheck()
                elif dec == '3':
                    print(f"\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                    idlechoice()
            elif dec == '3' and triangle_puzzle == False and 'Serrated Knife' not in player.inventory:
                dec = input(f"\nThere is an engraving on this podium, as well as a red button under a plastic cover that is held closed by a lock.\nNo key you have seen before can remove this lock.\nThe engraving reads:\n\n<The Hero with the {fc.CYAN}broken blade{fc.RESET} must sacrifice more than his {fc.CYAN}weapon{fc.RESET} to escape the {fc.RED}Devil{fc.RESET}.>\n\nYou're not quite sure what it means, but you feel like one of your items can be used here...\n\n{fc.BLACK}Which item would you like to try to use? (1:Damaged Screwdriver  2:Serrated Knife  3:Never mind){fc.RESET} ")
                acceptable = ['1','2']
                while dec not in acceptable:
                    dec = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}Which item would you like to try to use? (1:Damaged Screwdriver  2:Serrated Knife  3:Never mind){fc.RESET} ")
                if dec == '1':
                    triangle_puzzle = True
                    print(f"\nYou jam your {fc.CYAN}Damaged Screwdriver{fc.RESET} into the lock and begin to twist.\n\n{fc.RED}The screwdriver breaks in half, injuring your hand in the process! (-25 HP){fc.RESET}"); player.damage (25); player.remove_inventory_item('Damaged Screwdriver'); print(f"Your trusty screwdriver falls to the floor...\n\n{fc.GREEN}The lock has been opened!{fc.RESET}\n\n{fc.MAGENTA}You hurriedly push the button, and hear a click.{fc.RESET}")
                    podiumcheck()
                elif dec == '2':
                    print(f"\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                    idlechoice()
            elif dec == '3' and triangle_puzzle == True:
                print(f"\nThis is where you lost your trusty screwdriver.\n\n{fc.YELLOW}There is nothing left of interest here.{fc.RESET}")
                podiumcheck()
            elif dec == '4' and cross_puzzle == False:
                dec = input(f"\nThis podium has a beautiful velvet cover draped over it with a tag sticking out of the side of the cover.\n\nThe tag reads:\n\n<The {fc.MAGENTA}teeth{fc.RESET} used to break this lock are the same teeth that shall reveal this lock.>\n\n{fc.BLACK}What would you like to do? (1:Destroy the beautiful velvet cover  2:Walk away without feeling guilty about destroying something so beautiful){fc.RESET} ")
                acceptable = ['1','2']
                while dec not in acceptable:
                    dec = input(f"\n\n{fc.RED}Oh, come on, this one's easy.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Destroy the beautiful velvet cover  2:Walk away without feeling guilty about destroying something so beautiful){fc.RESET} ")                
                if dec == '1' and 'Serrated Knife' in player.inventory:
                    cross_puzzle = True
                    print(f"\nYou could not care less about someone else's hard work.\nYou pull out your {fc.CYAN}Serrated Knife{fc.RESET} and slash away at the innocent, beautiful velvet cover on the podium.\n\n{fc.GREEN}Congratulations on being a jerk, you found a red button!{fc.RESET}\n\n{fc.MAGENTA}You push the red button and hear a click!{fc.RESET}")
                    podiumcheck()
                elif dec == '1' and 'Serrated Knife' not in player.inventory:
                    print(f"\nYou could not care less about someone else's hard work, but you do not have an item you could use here.\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                elif dec == '2':
                    print(f"\nYou leave the beautiful velvet cover intact. {fc.RED}C O W A R D !{fc.RESET}\nBefore you can react, the velvet cover flies off of the podium and wraps itself around your face.\n\nWhy... do... you... smell... chloroform...? ...\n\n..................\n\nYou come to after a few minutes.\nThe sheer embarrassment of losing to a rug causes you to slap yourself in the face a bit too hard. {fc.RED}(-15 HP){fc.RESET}"); player.damage(15)
                    podiumcheck()
            elif dec == '4' and cross_puzzle == True:
                print(f"\n\n{fc.YELLOW}There is nothing left of interest here.{fc.RESET}")
                podiumcheck()
            elif dec == '5':
                print(f"\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
                idlechoice()
        elif square_puzzle == True and circle_puzzle == True and triangle_puzzle == True and cross_puzzle == True:
            loose_brick = True
            podiumcheck()


#Inspecting the golden podium
def goldenpodium():
    global seven_keys
    global all_keys
    global golden_podium_visited
    if golden_podium_visited == False and seven_keys == False:
        golden_podium_visited = True
        print(f"\nYou approach the {fc.YELLOW}golden{fc.RESET} podium to inspect it closer.\nThis mysterious lock box has many differently-shaped key holes.\nYou count seven.\n\nSince you do not have all of the keys, {fc.YELLOW}you decide to come back later.{fc.RESET}")
        idlechoice()
    elif golden_podium_visited == False and seven_keys == True:
        golden_podium_visited = True
        print(f"\nYou approach the {fc.YELLOW}golden{fc.RESET} podium to inspect it closer.")
        spade_key()
        all_keys = True
        idlechoice()
    elif golden_podium_visited == True and seven_keys == False:
        print(f"\nThe mysterious lock box continues to, well, stay locked.\n\n{fc.YELLOW}You decide to come back once you have all of the keys.{fc.RESET}")
        idlechoice()
    elif golden_podium_visited == True and seven_keys == True and all_keys == False:
        spade_key()
        all_keys = True
        idlechoice()
    elif all_keys == True:
        spade_key()
        idlechoice()


#Unlocking the hatch
def hatch_unlock():
    if all_keys == True:
        print(f"\nReacting to the power of the {fc.BLACK}{st.BRIGHT}mind{fc.RESET}{st.NORMAL}, {fc.YELLOW}body{fc.RESET}, {fc.RED}heart{fc.RESET}, and {fc.MAGENTA}soul{fc.RESET}, the door slowly opens.\n\n{fc.GREEN}You have successfully unlocked the hatch!{fc.RESET}\nYou slowly peek your head inside.\nYou can hardly believe your eyes.\nAt the end of a short tunnel, you see what appears to be a parking garage.\nYou climb down the hatch and run straight for the parking garage.\nYou find an unattended police cruiser with the keys sitting in the driver-side door.\nYou can't believe your luck.\nYou unlock the door, climb in the car, buckle up, and start the engine. The engine purs.\nYou yell out in excitement, then let out a massive sigh of relief.\nYou pull out of the parking spot, and head for the exit... ")
        if player.health >= 50:
            print(f"\n\n...nothing can stop you now.\n\nYou safely exit the parking garage and drive off into the sunset.\n\n\n\nC O N G R A T U L A T I O N S !\n\n")
            print(f"{fc.GREEN}{st.BRIGHT}----------------------------------------------------------------------------------\n*    *  *    *  *****   *    *      *       ****   *     *   *      *****   ***** \n*    *  **   *  *       *    *     * *     *       *   *     *      *       *    *\n*    *  * *  *  *****   ******    *   *    *       ****      *      *****   *    *\n*    *  *  * *      *   *    *   *******   *       *   *     *      *       *    *\n ****   *   **  *****   *    *  *       *   ****   *     *   *****  *****   ***** \n----------------------------------------------------------------------------------{fc.RESET}{st.NORMAL}")
            print(f"\n\n\n\n{fc.RED}T{fc.RESET} H {fc.RED}A{fc.RESET} N {fc.RED}K{fc.RESET}   Y {fc.RED}O{fc.RESET} U   {fc.RED}S{fc.RESET} O   {fc.RED}M{fc.RESET} U {fc.RED}C{fc.RESET} H   {fc.RED}F{fc.RESET} O {fc.RED}R{fc.RESET}   T {fc.RED}O{fc.RESET}   P {fc.RED}L{fc.RESET} A {fc.RED}Y{fc.RESET} I {fc.RED}N{fc.RESET} G   {fc.RED}M{fc.RESET} Y   {fc.RED}G{fc.RESET} A {fc.RED}M{fc.RESET} E   {fc.RED}!{fc.RESET} ! {fc.RED}!{fc.RESET}")
            quit()
        elif player.health >= 25 and player.health < 50:
            print(f"\n\n...your adrenaline starts to wear off.\nAfter barely managing to pull the heavy hatch open and running down that tunnel, you realize how weak you feel.\nYou park the car for a moment to try to catch your breath.\nAfter a few minutes go by, you think you're feeling better.\nYou turn the car back on.\nThe engine roars.\nThe exit isn't far, you tell yourself.\nYou adjust the gear shift.\nYou put the pedal to the metal...\n...you accidentally put the car in reverse and smash into the wall of the parking garage.\nThe ground starts quaking.\nYou start to panic.\nThe parking garage collapses over your head...\n\n\n{fc.RED}...and you're never heard from again...{fc.RESET}")
            print(f"\n\n{fc.RED}{st.BRIGHT}------------------------------------------------------------------\n*****   *    *      *       ****   *     *   *      *****   *****\n*       *    *     * *     *       *   *     *      *       *    *\n*****   ******    *   *    *       ****      *      *****   *    *\n    *   *    *   *******   *       *   *     *      *       *    *\n*****   *    *  *       *   ****   *     *   *****  *****   *****\n------------------------------------------------------------------\n\n{fc.RED}### G A M E   O V E R ###{fc.RESET}")
            quit()
        elif player.health < 25:
            print(f"\n\n...you open your eyes.\nYou're laying on the rug next to the hatch.\nYou were certain that you were just in a police cruiser, but you're back in the shack.\nThe hatch is open, and you peek back inside it.\nYour severely damaged body gives out on you, and you fall into the hatch head first.\nThere's a snap, then darkness...\n\n{fc.RED}...you really should have taken better care of your body...{fc.RESET}")
            print(f"\n\n{fc.RED}{st.BRIGHT}------------------------------------------------------------------\n*****   *    *      *       ****   *     *   *      *****   *****\n*       *    *     * *     *       *   *     *      *       *    *\n*****   ******    *   *    *       ****      *      *****   *    *\n    *   *    *   *******   *       *   *     *      *       *    *\n*****   *    *  *       *   ****   *     *   *****  *****   *****\n------------------------------------------------------------------\n\n{fc.RED}### G A M E   O V E R ###{fc.RESET}")
            quit()
    else:
        print(f"\n\n{fc.RED}You do not have the keys required to unlock the hatch.{fc.RESET}\n\n{fc.YELLOW}You decide to come back later.{fc.RESET}")
        idlechoice()


#Intro Entrance function
def entrance_intro():
    choice = input(f"\n\nYou have entered the shack as the door slams behind you.\nYou try to open the door, but it has been sealed shut.\nPanic kicks in for a moment, but then you remember your injury.\n{fc.MAGENTA}You need to patch yourself up.{fc.RESET}\nYou decide it would be best to have a look around to try to find some medical supplies.\nYou turn away from the door, and notice that this shack looks much larger than it did from the outside.\n\n{fc.BLACK}What would you like to do? (1:Enter another room  2:Search current room  3:Check status){fc.RESET} ")
    acceptable = ['1','2','3']
    while choice not in acceptable:
        choice = input(f"\n\n{fc.RED}Please enter a valid input.{fc.RESET}\n\n{fc.BLACK}What would you like to do? (1:Enter another room  2:Search current room  3:Check status){fc.RESET} ")
    if choice == '1':
        changerooms()
    elif choice == '2':
        roomscan()
    elif choice == '3':
        player.display_status()


#THE GAME STARTS HERE
west_status()
north_status()
east_status()
entrance_intro()
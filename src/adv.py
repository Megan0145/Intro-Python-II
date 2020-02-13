from room import Room
from player import Player
from item import Item 
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].add_item(Item("key", "used to open doors"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Megan", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def display_current_position():
    print(f'\nYour current position: \n{player.current_room.name}\n\nClue: \n{player.current_room.description}\n')
    print('Room Items:')
    i = 0
    for item in player.current_room.items:
        print(f'[{i}] : {item}')
        i += 1

def display_inventory():
    print('\nInventory:\n')
    for item in player.inventory:
        print(item.name)

def move_player():
    print("Select a direction to move in: ")
    for (key, value) in direction_options.items():
        print(f'[{key}] : {value}')
    selection = input()    
    if selection.upper() in direction_options:
        if getattr(player.current_room, f'{selection}_to') != None:
            player.current_room = getattr(player.current_room, f'{selection}_to')
        else:
            print("\nYou have reached a dead end :( Try turning back the way you came!") 
    else: 
        print("\nOops. Not a valid direction. Please try again.")    

def grab_item(item):
    for obj in player.current_room.items:
        if obj.name == item:
            player.current_room.remove_item(obj)
            player.grab_item(obj)
        else:
            print(f'Oops! {player.current_room.name} does not contain {item}. Try again.')  

def drop_item(item):
    for obj in player.inventory:
        if obj.name == item:
            player.drop_item(obj)
            player.current_room.add_item(obj)
        else:
            print(f'Oops! Your inventory does not contain {item}. Try again.')    

selection = ""

quit_game = False

direction_options = {
    'N' : 'North',
    'S' : 'South',
    'E' : 'East',
    'W' : 'West'
}

game_options = {
    'drop + item' : 'Drop an item in your inventory',
    'grab + item' : 'Grab an item in the current room',
    'm' : 'Move to a different room'
}

while quit_game == False:
    print("*" * 20)
    display_current_position()
    display_inventory()
    print("What would you like to do?")
    for (key, value) in game_options.items():
        print(f'[{key}] : {value}')
    print('[q] : Quit game')
    print("*" * 20) 
    selection = input()
    if selection == 'm':
        move_player()  
    elif selection[:4] == 'grab' or selection[:4] == 'drop':
        action = selection[:4]
        obj = selection[5:]
        if action == 'grab':
            grab_item(obj)
        elif action == 'drop':   
            drop_item(obj)
    elif selection == 'q':
       print(f'Thank you for playing, {player.name}. Goodbye!')
       quit_game = True
    else:
        print(f'Oops! not a valid game option. Try again')      
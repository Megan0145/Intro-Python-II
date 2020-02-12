from room import Room
from player import Player

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
    print(f'Your current position: \n{player.current_room.name}\nClue: \n{player.current_room.description}')

def move_player():
    if selection == "n":
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to 
        else:
            print("You have reached a dead end :( Try turning back the way you came!") 
    elif selection == "s":
        if player.current_room.s_to != None:
            player.current_room = player.current_room.s_to 
        else:
            print("You have reached a dead end :( Try turning back the way you came!") 
    elif selection == "e":
        if player.current_room.e_to != None:
            player.current_room = player.current_room.e_to 
        else:
            print("You have reached a dead end :( Try turning back the way you came!")    
    elif selection == "w":
        if player.current_room.w_to != None:
            player.current_room = player.current_room.w_to 
        else:
            print("You have reached a dead end :( Try turning back the way you came!")  
          
 

selection = ""

direction_options = {
    'n' : 'North',
    's' : 'South',
    'e' : 'East',
    'w' : 'West',
    'q' : 'Quit'
}


while selection != "q":
    display_current_position()
    print("Select a direction to move in: ")
    for (key, value) in direction_options.items():
        print(f'[{key}] : {value}')
    selection = input()
    if selection in direction_options:
        move_player() 
    else: 
        print("Oops. Not a valid direction. Please try again.")    
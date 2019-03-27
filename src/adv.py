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
p1 = Player('brooks', 'outside')
print(room['outside'])
room['outside'].addItem('staff', 'staff of warlords')
print(room['outside'].items)
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
val = input("welcome to the game! type your name to start:")
user = val
player = Player(user, 'outside')
location = room[player.currentRoom]
def logItems():
    print('\nroom items:\n')
    for i in location.items:
        try:
            print(i['item'])
        except: 
            pass
while not val == "q":
    val = val.lower()
    if val == 'help':
        val = input(bracket +"type a direction [N] [S] [E] or [W] to move your character through\n the mansion try your best to find the hidden treasure.\n enter any key to continue" + bracket)
    bracket = '\n*********************************************************************\n'
    print(bracket)
    print(player.currentRoom)
    print(location.description)
    
    logItems()
    print(bracket)
    if val == 'n':
        try:
            print(location.n_to.name)
            print(location.n_to.description)
            logItems()
            location = location.n_to
        except:
            print('cant go north here')
    if val == 's':
        try:
            print(location.s_to.name)
            print(location.s_to.description)
            logItems()
            location = location.s_to
        except:
            print('cant go south here')
    if val == 'e':
        try:
            print(location.e_to.name)
            print(location.e_to.description)
            logItems()
            location = location.e_to
        except:
            print('cant go east here')
    if val == 'w':
        try:
            print(location.w_to.name)
            print(location.w_to.description)
            logItems()
            location = location.w_to
        except:
            print('cant go west here')


    val = input(bracket + "\nWhat would you like to do? type 'help' if you need instructions:")
    
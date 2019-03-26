# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, username, currentRoom):
        self.username = username
        self.currentRoom = currentRoom
    def __str__(self):
        return str(self.__dict__)
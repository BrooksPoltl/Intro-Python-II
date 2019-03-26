# Write a class to hold player information, e.g. what room they are in
# currently.

class Room:
    def __init__(self, information, currentRoom):
        self.information = information
        self.currentRoom = currentRoom
    def __str__(self):
        return str(self.__dict__)
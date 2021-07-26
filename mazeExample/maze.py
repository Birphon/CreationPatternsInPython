# Maze.py

#CONSTANTS
N = 0
E = 1
S = 2
W = 3

oppositeDirection = {N:S, E:W, S:N, W:E}

class MapSite(object):
    def enter(self):
        raise NotImplemented
    
class Room(MapSite):
    def __init__(self, roomNumber):
        self.roomNumber = roomNumber
        self.sides = [0,0,0,0]
    def setSide(self, direction,mapSite):
        self.sides[direction] = mapSite
    def getSide(self, direction):
        return self.sides[direction]
    def enter(self):
        pass
    def __str__(self):
        return 'room#' + str(self.roomNumber) + ' '.join([str(side) \
                for side in self.sides])

class Wall(MapSite):
    def __str__(self):
        return ' Wall'

class Door(MapSite):
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2
        self.isOpen = 1
    def __str__(self):
        if self.isOpen:
            return ' Open-door'
        else:
            return ' Closed-door'
        
class Maze(object):
    def __init__(self):
        self.rooms = []
    def addRoom(self, room):
        self.rooms.append(room)
    def roomNumber(self, roomNumber):
        for room in self.rooms:
            if room.roomNumber == roomNumber:
                return room
        return None
    def __str__(self):
        return '\n'.join([str(room) for room in self.rooms])
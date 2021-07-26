# python buildermaze.py
from maze import *

class MazeBuilder(object):
    """ a base class which defines an interface """
    def buildRoom(self, roomNumber):
        pass
    def buildDoor(self, roomNumber1, roomNumber2, room1DoorSide = N):
        pass
    def getMaze(self):
        return None

class StandardMazeBuilder(MazeBuilder):
    """ a subclass of Builder which does actual work     """
    def __init__(self):
        self.currentMaze = Maze()
    def getMaze(self):
        return self.currentMaze
    def buildRoom(self, roomNumber):
        if (self.currentMaze.roomNumber(roomNumber) == None) :
            room = Room(roomNumber)
            self.currentMaze.addRoom(room)
            room.setSide(N, Wall())
            room.setSide(E, Wall())
            room.setSide(S, Wall())
            room.setSide(W,Wall())
    def buildDoor(self, roomNumber1, roomNumber2, room1DoorSide = N):
        room1 = self.currentMaze.roomNumber(roomNumber1)
        room2 = self.currentMaze.roomNumber(roomNumber2)
        door = Door(room1, room2)
        room1.setSide(room1DoorSide, door)
        room2.setSide(oppositeDirection[room1DoorSide], door)

class CountingMazeBuilder(MazeBuilder):
    """ alternative subclass of builder with different effects """
    def __init__(self):
        self.counts = {'rooms': 0, 'doors' : 0}
    def buildRoom(self, roomNumber):
        self.counts['rooms'] += 1
    def buildDoor(self, roomNumber1, roomNumber2, room1DoorSide = N):
        self.counts['doors'] += 1
    def getMaze(self):
        return self.counts
    
class MazeGame:
    def __init__(self, builder):
        self.maze = self.createMaze(builder)
    def createMaze(self, builder):
        builder.buildRoom(1)
        builder.buildRoom(2)
        builder.buildDoor(1, 2, S)
        return builder.getMaze()
    def __str__(self):
        return str(self.maze)

if __name__ == "__main__":
    print "\n"
    print MazeGame( StandardMazeBuilder() )
    print MazeGame( CountingMazeBuilder() )

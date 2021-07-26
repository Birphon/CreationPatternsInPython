# maze implemented with FactoryMethod
from maze import *
class FactorymethodMazeGame(object):
    # factory methods to return components of a given type
    def makeMaze(self):
        return Maze()
    def makeRoom(self, roomNumber):
        return Room(roomNumber)
    def makeWall(self):
        return Wall()
    def makeDoor(self, room1, room2):
        return Door(room1, room2)
    def createMaze(self):
        """ a default implementation returning simplest type of maze """
        self.maze = self.makeMaze()
        r1 = self.makeRoom(1)
        r2 = self.makeRoom(2)
        door = self.makeDoor(r1, r2)
        self.maze.addRoom(r1)
        self.maze.addRoom(r2)
        r1.setSide(N, self.makeWall())
        r1.setSide(E, door)
        r1.setSide(S, self.makeWall())
        r1.setSide(W, self.makeWall())
        r2.setSide(N, self.makeWall())
        r2.setSide(E, self.makeWall())
        r2.setSide(S, self.makeWall())
        r2.setSide(W, door)
    def __init__(self):
        """ the constuctor is vectored """
        self.createMaze()
    def __str__(self):
        return str(self.maze)
# now subclassing specializes parts of the maze
class RoomWithABomb(Room):
    def __init__(self,roomNumber):
        self.hasBomb = 1
        # parent class __init__ needs to be explicitly called!
        Room.__init__(self,roomNumber)
    def __str__(self):
        s = 'BOMBEDroom#' + str(self.roomNumber)
        for mapsite in self.sides:
            s = s + str(mapsite)
        if self.hasBomb:
            s = s + ' and a bomb is in the room'
        return s
# override the factory method for different behaviour        
class BombedMazeGame(factorymethodMazeGame):
    def makeRoom(self,roomNumber):
        return RoomWithABomb(roomNumber)
    
if __name__ == '__main__':
    print "\nStandard Maze"
    m = factorymethodMazeGame()
    print m
    print "\nBombed Maze"
    m = BombedMazeGame()
    print m
"""
Standard Maze
room#1 Wall  Open-door  Wall  Wall
room#2 Wall  Wall  Wall  Open-door

Bombed Maze
BOMBEDroom#1 Wall Open-door Wall Wall and a bomb is in the room
BOMBEDroom#2 Wall Wall Wall Open-door and a bomb is in the room
"""
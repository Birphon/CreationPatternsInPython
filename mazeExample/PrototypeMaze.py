from maze import *
import copy

class MazeFactory(object):
    """ a factory class which creates components of mazes """
    def makeMaze(self):
        return Maze()
    def makeWall(self):
        return Wall()
    def makeRoom(self, roomNumber):
        return Room(roomNumber)
    def makeDoor(self, room1, room2):
        return Door(room1, room2)
    
class MazeGame(object):
    def createMaze(self, mazeFactory):
        self.maze = mazeFactory.makeMaze()
        room1 = mazeFactory.makeRoom(1)
        room2 = mazeFactory.makeRoom(2)
        door = mazeFactory.makeDoor(room1, room2)
        self.maze.addRoom(room1)
        self.maze.addRoom(room2)
        room1.setSide(N, mazeFactory.makeWall())
        room1.setSide(E, door)
        room1.setSide(S, mazeFactory.makeWall())
        room1.setSide(W, mazeFactory.makeWall())
        room2.setSide(N, mazeFactory.makeWall())
        room2.setSide(E, mazeFactory.makeWall())
        room2.setSide(S, mazeFactory.makeWall())
        room2.setSide(W, door)
    def __init__(self, mazeFactory):
        self.createMaze(mazeFactory)
    def __str__(self):
        return str(self.maze)
    
class RoomWithABomb(Room):
    def __init__(self, roomNumber):
        self.hasBomb = 1
        # parent class __init__ needs to be explicitly called!
        Room.__init__(self, roomNumber)
    def __str__(self):
        s = 'BOMBEDroom#' + str(self.roomNumber)
        for mapsite in self.sides:
            s = s + str(mapsite)
        if self.hasBomb:
            s = s + ' and a bomb is in the room'
        return s
    
# a prototype factory
class MazePrototypeFactory(MazeFactory):
    def __init__(self, prototypeMaze, prototypeWall, prototypeRoom, prototypeDoor):
        self.prototypeMaze = prototypeMaze
        self.prototypeWall = prototypeWall
        self.prototypeRoom = prototypeRoom
        self.prototypeDoor = prototypeDoor
    def makeMaze(self):
        return copy.deepcopy(self.prototypeMaze)
    def makeDoor(self, room1, room2):
        door = copy.deepcopy(self.prototypeDoor)
        door.__init__(room1, room2)
        return door
    def makeWall(self):
        return copy.deepcopy(self.prototypeWall)
    def makeRoom(self, roomNumber):
        room = copy.deepcopy(self.prototypeRoom)
        room.__init__(roomNumber)
        return room    

if __name__ == "__main__":
    print "\n" + "straight from the factory"
    m = MazeGame( MazeFactory() )
    print m
    print "\n" + "same from prototypes"
    f = MazeFactory()
    maze = f.makeMaze()
    r = f.makeRoom( 1 )
    d = f.makeDoor(r,r)
    w = f.makeWall()
    m = MazeGame( MazePrototypeFactory(maze,w,r,d) )
    print m
    print "\n" + "changed a prototype"
    r = RoomWithABomb(1)
    m = MazeGame( MazePrototypeFactory(maze,w,r,d) )
    print m
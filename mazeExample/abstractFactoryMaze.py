from maze import MapSite, Room, Wall, Door, Maze, N, S, W, E

# a factory class which creates components of mazes
class MazeFactory(object):
    def makeMaze(self):
        return Maze()
    def makeWall(self):
        return Wall()
    def makeRoom(self, roomNumber):
        return Room(roomNumber)
    def makeDoor(self, room1, room2):
        return Door(room1, room2)
    
class MazeGame(object):
    def createMaze( self, mazeFactory):
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
    
# a more specialized factory
class BombedMazeFactory(MazeFactory):
    def makeRoom(self, roomNumber):
        return RoomWithABomb(roomNumber)
    
if __name__ == '__main__':
    m = MazeGame(MazeFactory())
    print m
    print "\n"
    m = MazeGame(BombedMazeFactory())
    print m

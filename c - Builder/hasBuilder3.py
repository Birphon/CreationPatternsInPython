"""
REPLACE THIS LINE WITH YOUR NAME

TASK:   (1) redesign this system so it uses the BUILDER GOF pattern
        (2) add the additional output option mentioned at the end
"""

class AbstractBuilder(object):
    def __init__(self):
        self.maze = []
    def getResult(self):
        return self.maze
    def addWall(self, side):
        pass
    def addRoom(self, id):
        pass
    def addDoor(self, side):
        pass
class NormalMazeBuilder(AbstractBuilder):
    def addWall(self, side):
        self.maze.append( "a wall on the " + side)
    def addRoom(self, id):
        self.maze.append( "Room #" + str(id) )
    def addDoor(self, side):
        self.maze.append( "a door on the " + side )   

class Director(object):
    def __init__(self, builder):
        self.builder = builder
    def constructMaze(self):
        self.builder.addRoom( 1 )
        self.builder.addWall( "N" )
        self.builder.addWall( "S" )
        self.builder.addWall( "W" )
        self.builder.addDoor( "E" )
        return self.builder.getResult()
    
class Maze(object):
    def __init__(self):
        self.maze = []
    def add( self, type, id=0, side="N" ):
        """This design is inflexible.
            The case statement in this method
            will forever have to be edited and extended
        """
        if type == 'WALL':
            self.maze.append( "a wall on the " + side)
        elif type == 'ROOM':
            self.maze.append( "Room #" + str(id) )
        elif type == 'DOOR':
            self.maze.append( "a door on the " + side )


if __name__ == "__main__":
    builder = NormalMazeBuilder()
    director = Director(builder)
    #director = Director(NormalMazeBuilder())
    print(director.constructMaze())
    #['Room #1', 'a wall on the N', 'a wall on the S', 'a wall on the W', 'a door on the E']
    
"""
additional functionality required is
same input but a count of things created
# {'WALL': 4, 'DOOR': 1, 'ROOM': 1}
""" 
"""
REPLACE THIS LINE WITH YOUR NAME

TASK:   (1) redesign this system so it uses the BUILDER GOF pattern
        (2) add the additional output option mentioned at the end
"""
class Maze(object):
    def __init__(self):
        self.doorCount = 0
        self.wallCount = 0
        self.roomCount = 0
    def getMaze(self):
        maze = []
        maze.append( "ROOM=" + str(self.roomCount) )
        maze.append( "WALL=" + str(self.wallCount) )
        maze.append( "DOOR=" + str(self.doorCount) )
        return maze
    def add( self, type, id=0, side="N" ):
        """This design is inflexible.
            The case statement in this method
            will forever have to be edited and extended
        """
        if type == 'WALL':
            self.wallCount += 1
        elif type == 'ROOM':
            self.roomCount += 1
        elif type == 'DOOR':
            self.doorCount += 1


if __name__ == "__main__":
    maze = Maze()
    maze.add( "ROOM", 1 )
    maze.add( "WALL", 0, "N" )
    maze.add( "WALL", 0, "S" )
    maze.add( "WALL", 0, "W" )
    maze.add( "DOOR", 0, "E" )
    print(maze.getMaze())
    #['ROOM=1', 'WALL=3', 'DOOR=1']
    
"""
additional functionality required is
same input but a DESCRIPTION of things created
#['Room #1', 'a wall on the N', 'a wall on the S', 'a wall on the W', 'a door on the E']

""" 
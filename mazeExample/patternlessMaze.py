# patternlessMaze.py
from maze import *

# simple maze game with no design patterns
# a hard coded maze which does not provide for much reuse
class MazeGame(object):
    def createMaze(self):
        self.maze = Maze()
        r1 = Room(1)
        r2 = Room(2)
        door = Door(r1, r2)
        self.maze.addRoom(r1)
        self.maze.addRoom(r2)
        r1.setSide(N, Wall())
        r1.setSide(E, door)
        r1.setSide(S, Wall())
        r1.setSide(W, Wall())
        r2.setSide(N, Wall())
        r2.setSide(E, Wall())
        r2.setSide(S, Wall())
        r2.setSide(W, door)
    def __init__(self):
        self.createMaze()
    def __str__(self):
        return str(self.maze)

if __name__ == '__main__':
    print("\nStandard Maze")
    m = MazeGame()
    print(m)

"""
Standard Maze
room#1 Wall  Open-door  Wall  Wall
room#2 Wall  Wall  Wall  Open-door
"""
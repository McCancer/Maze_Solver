from Window import *
from Maze import *
from Cell import *

def main():
     win = Window(800, 600)
     our_maze = Maze(20, 2, 5, 5, 100, 100, win)
     our_maze.solve()
     win.wait_for_close()


if __name__ == "__main__":
    main()
from Window import *
from Maze import *
from Cell import *

def main():
     win = Window(800, 600)
     our_maze = Maze(20, 2, 5, 5, 100, 100, win, 0)
     our_maze._break_entrance_and_exit()
     our_maze._break_walls_r(0,0)
     win.wait_for_close()


if __name__ == "__main__":
    main()
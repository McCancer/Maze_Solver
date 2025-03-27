from Cell import Cell
from Window import Point
import time
import random

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x = x1
        self.y = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cx = cell_size_x
        self.cy = cell_size_y
        self.win = win
        self.__create_cells()

    def __create_cells(self):
        self._cells = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for i in range(self.num_cols):
            xpos = (self.cx * i) + self.x
            xpos2 = xpos + self.cx
            for j in range(self.num_rows):
                ypos = (self.cy * j) + self.y
                ypos2 = self.cy + ypos
                self._cells[i][j] = Cell(Point(xpos, ypos), Point(xpos2, ypos2), self.win)
                self.__draw_cell(i,j)

    def __draw_cell(self, i ,j):
        if self.win is None:
            return
        self._cells[i][j].draw()
        self.__animate()

    def __animate(self):
        if self.win is None:
            return 
        self.win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        entranceRandom = random.randint(1,2)
        exitRandom = random.randint(1,2)
        if(entranceRandom == 1):
            #left wall gone
            self._cells[0][0].has_left_wall = False
        else:
            self._cells[0][0].has_top_wall = False
        if(exitRandom == 1):
            self._cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        else:
            self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.__draw_cell(0,0)
        self.__draw_cell(self.num_cols-1,self.num_rows-1)

def main():
    pass

if __name__ == "__main__":
    main()
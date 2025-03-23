from Cell import Cell
from Window import Point
import time

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x = x1
        self.y = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cx = cell_size_x
        self.cy = cell_size_y
        self.win = win
        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for i in range(self.num_cols):
            xpos = (self.cx * i) + self.x
            xpos2 = xpos + self.cx
            for j in range(self.num_rows):
                ypos = (self.cy * j) + self.y
                ypos2 = self.cy + ypos
                self.__cells[i][j] = Cell(Point(xpos, ypos), Point(xpos2, ypos2), self.win)
                self.__draw_cell(i,j)

    def __draw_cell(self, i ,j):
        self.__cells[i][j].draw()

    def __animate(self):
        self.win.redraw()
        time.sleep(0.05)

def main():
    pass

if __name__ == "__main__":
    main()
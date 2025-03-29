from Cell import Cell
from Window import Point
import time
import random

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x = x1
        self.y = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cx = cell_size_x
        self.cy = cell_size_y
        self.win = win
        if seed is not None:
            random.seed(seed)
        self.__create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cell_visited()

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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while(True):
            to_visit = []
            #Check Cells
            if(i+1 < self.num_cols and (not self._cells[i+1][j].visited)):
                #right
                to_visit.append((i+1, j))
            if(i-1 >= 0 and (not self._cells[i-1][j].visited)):
                #left
                to_visit.append((i-1, j))
            if(j+1 < self.num_rows and (not self._cells[i][j+1].visited)):
                #bottom
                to_visit.append((i, j+1))
            if(j-1 >= 0 and (not self._cells[i][j-1].visited)):
                #top
                to_visit.append((i, j-1))
            #See if we can break
            if len(to_visit) == 0:
                self.__draw_cell(i,j)
                return 
            #find cell to go to
            direction = to_visit[random.randint(0, len(to_visit)-1)]
            #Break down the walls
            if(direction[0] > i):
                #right
                self._cells[i][j].has_right_wall = False
                self._cells[direction[0]][direction[1]].has_left_wall = False
            elif(direction[0] < i):
                #left
                self._cells[i][j].has_left_wall = False
                self._cells[direction[0]][direction[1]].has_right_wall = False
            elif(direction[1] > j):
                #bottom
                self._cells[i][j].has_bottom_wall = False
                self._cells[direction[0]][direction[1]].has_top_wall = False
            elif(direction[1] < j):
                #top
                self._cells[i][j].has_top_wall = False
                self._cells[direction[0]][direction[1]].has_bottom_wall = False
            else:
                raise Exception("Direction in break walls is invalid")
            #move to chosen cell
            self._break_walls_r(direction[0], direction[1])

    def _reset_cell_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False
            
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self.__animate()
        self._cells[i][j].visited = True
        if(i == self.num_cols-1 and j == self.num_rows-1):
            return True
        if(i+1 < self.num_cols and (not self._cells[i+1][j].visited) and (not self._cells[i][j].has_right_wall)):
            #right
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if(self._solve_r(i+1,j)):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], True)
        if(i-1 >= 0 and (not self._cells[i-1][j].visited) and (not self._cells[i][j].has_left_wall)):
            #left
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if(self._solve_r(i-1,j)):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], True)
        if(j+1 < self.num_rows and (not self._cells[i][j+1].visited) and (not self._cells[i][j].has_bottom_wall)):
            #bottom
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if(self._solve_r(i,j+1)):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], True)
        if(j-1 >= 0 and (not self._cells[i][j-1].visited) and (not self._cells[i][j].has_top_wall)):
            #top
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if(self._solve_r(i,j-1)):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], True)    
        return False
        

def main():
    pass

if __name__ == "__main__":
    main()
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Main Window"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running is True:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, Line, fill_color):
        Line.draw(self.canvas,fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2

    def draw(self, Canvas, fill_color):
        Canvas.create_line(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, pt1, pt2, can):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.top_left_point = pt1
        self.bottom_right_point = pt2
        self.__win = can

    def draw(self):
        pt_bottom_left = Point(self.top_left_point.x, self.bottom_right_point.y)
        pt_top_right = Point(self.bottom_right_point.x, self.top_left_point.y)
        if(self.has_left_wall):
            self.__win.draw_line(Line(self.top_left_point, pt_bottom_left), 'black')
        if(self.has_right_wall):
            self.__win.draw_line(Line(self.bottom_right_point, pt_top_right), 'black')
        if(self.has_top_wall):
            self.__win.draw_line(Line(self.top_left_point, pt_top_right), 'black')
        if(self.has_bottom_wall):
            self.__win.draw_line(Line(self.bottom_right_point, pt_bottom_left), 'black')
    
    def getCenterPoint(self):
        center_x = (self.bottom_right_point.x + self.top_left_point.x)//2
        center_y = (self.bottom_right_point.y + self.top_left_point.y)//2
        return Point(center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        fill_color = "grey"
        if undo:
            fill_color = "red"
        self_center = self.getCenterPoint()
        to_cell_center = to_cell.getCenterPoint()
        self.__win.draw_line(Line(self_center, to_cell_center), fill_color)
        

def main():
    win = Window(800, 600)
    pt1 = Point(100, 200)
    pt2 = Point(200, 500)
    pt3 = Point(400, 200)
    pt4 = Point(500, 500)
    cell1 = Cell(pt1, pt2, win)
    cell1.draw()
    cell2 = Cell(pt3, pt4, win)
    cell2.draw()
    cell1.draw_move(cell2, True)
    win.wait_for_close()

if __name__ == "__main__":
    main()
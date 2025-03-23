from Window import Point, Line

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
    pass

if __name__ == "__main__":
    main()
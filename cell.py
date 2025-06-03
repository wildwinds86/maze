from graphics import Point, Line


class Cell:
    def __init__(self, window=None):
        self.right_wall = None
        self.bottom_wall = None
        self.left_wall = None
        self.top_line = None

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.__win = window
        self.visited = False

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_centre(self):
        return Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)

    def draw_move(self, to_cell, undo=False):
        start = self.get_centre()
        end = to_cell.get_centre()
        l = Line(start, end)
        if undo:
            fill = "gray"
        else:
            fill = "red"
        self.__win.draw_line(l, fill)

    def draw(self, x1, y1, x2, y2):
        self.set_coords(x1, y1, x2, y2)
        self.top_line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
        self.bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
        self.left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
        self.right_wall = Line(Point(self.__x2, self.__y2), Point(self.__x2, self.__y1))

        if self.has_top_wall:
            self.__win.draw_line(self.top_line)
        else:
            self.__win.draw_line(self.top_line, "white")

        if self.has_bottom_wall:
            self.__win.draw_line(self.bottom_wall)
        else:
            self.__win.draw_line(self.bottom_wall, "white")

        if self.has_left_wall:
            self.__win.draw_line(self.left_wall)
        else:
            self.__win.draw_line(self.left_wall, "white")

        if self.has_right_wall:
            self.__win.draw_line(self.right_wall)
        else:
            self.__win.draw_line(self.right_wall, "white")

    def redraw(self):
        if self.__win is None:
            return

        if self.has_top_wall:
            self.__win.draw_line(self.top_line)
        else:
            self.__win.draw_line(self.top_line, "white")

        if self.has_bottom_wall:
            self.__win.draw_line(self.bottom_wall)
        else:
            self.__win.draw_line(self.bottom_wall, "white")

        if self.has_left_wall:
            self.__win.draw_line(self.left_wall)
        else:
            self.__win.draw_line(self.left_wall, "white")

        if self.has_right_wall:
            self.__win.draw_line(self.right_wall)
        else:
            self.__win.draw_line(self.right_wall, "white")

    def break_wall(self, direction):
        match direction:
            case "top":
                self.has_top_wall = False
            case "bottom":
                self.has_bottom_wall = False
            case "left":
                self.has_left_wall = False
            case "right":
                self.has_right_wall = False

        self.redraw()

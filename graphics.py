from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill="black"):
        line.draw(self.__canvas, fill)
        

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill, width = 5
        )

class Cell():
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

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

        if self.has_top_wall:
            self.top_line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(self.top_line)

        if self.has_bottom_wall:
            self.bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(self.bottom_wall)

        if self.has_left_wall:
            self.left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(self.left_wall)

        if self.has_right_wall:
            self.right_wall = Line(Point(self.__x2, self.__y2), Point(self.__x2, self.__y1))
            self.__win.draw_line(self.right_wall)

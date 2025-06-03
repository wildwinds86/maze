import time
import random
from cell import Cell


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []

        if not seed:
            random.seed(seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_visited()



    def __create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self.__cells.append(col_cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        if self.win is None: return
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.animate()

    def __break_entrance_and_exit(self):
        self.__cells[0][0].break_wall("top")
        self.__cells[-1][-1].break_wall("bottom")

    def animate(self):
        if self.win is None: return
        self.win.redraw()
        time.sleep(0.05)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            next_index_list = []

            #determine cells to visit next
            #left
            if i > 0 and not self.__cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))

            #right
            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))

            #up
            if j > 0 and not self.__cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))

            #down
            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                self.__draw_cell(i, j)
                return

            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            if next_index[0] == i + 1:
                self.__cells[i][j].break_wall("right")
                self.__cells[i + 1][j].break_wall("left")

            if next_index[0] == i - 1:
                self.__cells[i][j].break_wall("left")
                self.__cells[i - 1][j].break_wall("right")

            if next_index[1] == j + 1:
                self.__cells[i][j].break_wall("bottom")
                self.__cells[i][j + 1].break_wall("top")

            if next_index[1] == j - 1:
                self.__cells[i][j].break_wall("top")
                self.__cells[i][j - 1].break_wall("bottom")

            self.__break_walls_r(next_index[0], next_index[1])

    def __reset_visited(self):
        for i in self.__cells:
            for j in i:
                j.visited = False

        pass
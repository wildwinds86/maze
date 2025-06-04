from graphics import *
from maze import *
import sys


def main():
    num_rows = 16
    num_cols = 25
    margin = 50
    screen_x = 2560
    screen_y = 1600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)

    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze has been created!")

    is_solvable = maze.solve()

    if not is_solvable:
        print("Maze cannot be solved :(")
    else:
        print("Maze has been solved!")

    win.wait_for_close()


main()

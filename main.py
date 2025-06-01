from graphics import *

def main():
    win = Window(800, 600)
    

    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 300)
    p4 = Point(300, 400)
    line = Line(p1, p2)
    line2 = Line(p3, p4)
    
    win.draw_line(line, "red")
    win.draw_line(line2, "red")

    win.wait_for_close()

main()

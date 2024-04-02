from tkinter import *


class Window:
    def __init__(self):
        self.root = Tk()

        self.root.geometry("%dx%d+0+0" % (400, 300))
        self.root.mainloop()


if __name__ == "__main__":
    Window()

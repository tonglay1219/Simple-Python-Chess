import Tkinter as tk  # python 2
import tkFont as tkfont  # python 2
import gui_tkinter
import os
from board import Board
from random import randint


class FrameHelper(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (WelcomeWindow, TraditionalMode, NewMode):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomeWindow")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        self.frame = self.frames[page_name]
        self.frame.tkraise()
        if page_name == "TraditionalMode" or page_name == "NewMode":
            self.frame.show()


class WelcomeWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Chess")
        self.label.pack(side="top", fill="x", pady=10)

        self.button1 = tk.Button(self, text="Traditional Mode", name="traditional_btn",
                            command=lambda: controller.show_frame("TraditionalMode"))
        self.button2 = tk.Button(self, text="New Mode", name="new_mode_btn",
                            command=lambda: controller.show_frame("NewMode"))
        self.button1.pack()
        self.button2.pack()


class TraditionalMode(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def show(self):
        gui = gui_tkinter.BoardGuiTk(self.controller, Board())
        gui.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        gui.draw_pieces()


class NewMode(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def show(self):
        gui = gui_tkinter.BoardGuiTk(self.controller, Board(get_random_rule()))
        gui.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        gui.draw_pieces()


def get_random_rule():
    rules = open(os.path.dirname(os.path.abspath(__file__)) + "/960rules.txt").readlines()
    return rules[randint(0, len(rules))]


if __name__ == "__main__":
    app = FrameHelper()
    app.mainloop()

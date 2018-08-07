import Tkinter as tk  # python 2
import tkFont as tkfont  # python 2
import gui_tkinter
from board import Board


class FrameHelper(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (WelcomeWindow, TraditionalMode, NewMode):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomeWindow")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "TraditionalMode":
            frame.show()


class WelcomeWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Chess")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Traditional Mode",
                            command=lambda: controller.show_frame("TraditionalMode"))
        button2 = tk.Button(self, text="New Mode",
                            command=lambda: controller.show_frame("NewMode"))
        button1.pack()
        button2.pack()


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
        pass


if __name__ == "__main__":
    app = FrameHelper()
    app.mainloop()

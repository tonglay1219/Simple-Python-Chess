import unittest
import Tkinter as tk
import chesslib
from chesslib.gui_tkinter import *
from chesslib.gui_console import display
from chesslib.welcome_window import *
from chesslib.board import Board


class Test(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.board = BoardGuiTk(root, Board())

    def tearDown(self):
        pass

    def test_save_btn(self):
        self.board.button_save.invoke()

    def test_960rule(self):
        rule = get_random_rule()
        print(rule)

    def test_canves_size(self):
        self.assertEqual(self.board.canvas_size, (512, 512))

    def test_welcome_window(self):
        FrameHelper()

    def test_quit_btn(self):
        self.board.button_quit.invoke()

if __name__ == '__main__':
    unittest.main()

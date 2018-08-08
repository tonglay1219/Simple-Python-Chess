import unittest
from pprint import pprint
from chesslib.gui_tkinter import *
from chesslib.welcome_window import *
from chesslib.board import Board


class Test(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.mapping_960 = get_random_rule()
        # print(self.mapping_960)
        self.board = BoardGuiTk(root, Board())
        self.board_960 = BoardGuiTk(root, Board(self.mapping_960))
        self.alphabets = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def tearDown(self):
        pass

    def test_save_btn(self):
        self.board.button_save.invoke()

    def test_960rule(self):
        rule = get_random_rule()

    def test_canves_size(self):
        self.assertEqual(self.board.canvas_size, (512, 512))

    def test_welcome_window(self):
        FrameHelper()

    def test_quit_btn(self):
        self.board.button_quit.invoke()

    def test_correct_piece_for_tranditional_mode(self):
        set_up_string = "rnbqkbnr"
        incorrect_position = False
        for i in range(0, 8):
            current_letter = self.alphabets[i]
            current_chess_white = self.board.chessboard.get(current_letter.upper() + str(1)).abbriviation
            current_chess_black = self.board.chessboard.get(current_letter.upper() + str(8)).abbriviation
            pawn_white = self.board_960.chessboard.get(current_letter.upper() + str(2)).abbriviation
            pawn_black = self.board_960.chessboard.get(current_letter.upper() + str(7)).abbriviation
            self.assertEqual(pawn_white.lower(), "p")
            self.assertEqual(pawn_black.lower(), "p")
            self.assertEqual(current_chess_black.lower(), set_up_string[i])
            self.assertEqual(current_chess_white.lower(), set_up_string[i])

    def test_correct_piece_for_960_mode(self):
        set_up_string = self.mapping_960.split("/")[0]
        incorrect_position = False
        for i in range(0, 8):
            current_letter = self.alphabets[i]
            current_chess_white = self.board_960.chessboard.get(current_letter.upper() + str(1)).abbriviation
            current_chess_black = self.board_960.chessboard.get(current_letter.upper() + str(8)).abbriviation
            pawn_white = self.board_960.chessboard.get(current_letter.upper() + str(2)).abbriviation
            pawn_black = self.board_960.chessboard.get(current_letter.upper() + str(7)).abbriviation
            self.assertEqual(pawn_white.lower(), "p")
            self.assertEqual(pawn_black.lower(), "p")
            self.assertEqual(current_chess_black.lower(), set_up_string[i])
            self.assertEqual(current_chess_white.lower(), set_up_string[i])

    def get_board_mapping(self):
        return {"Rook": "r", "Knight": "n", "Bishop": "b", "Queen": "q", "King": "k", "Pawn": "p"}


if __name__ == '__main__':
    unittest.main()

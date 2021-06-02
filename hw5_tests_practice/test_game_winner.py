import unittest
from game import TicTacToe


class TestWinner(unittest.TestCase):

    def setUp(self):
        self.game_unittest = TicTacToe()

    def test_row_unittest(self):
        print("Checking row")
        self.game_unittest.board = ["X", "0", "X",
                                    " ", "0", "0",
                                    "X", "0", "X"]
        self.assertTrue(self.game_unittest.winner("0", 2))
        print(self.game_unittest.board)

    def test_column_unittest(self):
        print("Checking column")
        self.game_unittest.board = ["X", "0", "X",
                                    " ", "0", "0",
                                    "0", "0", "X"]
        self.assertTrue(self.game_unittest.winner("0", 5))
        print(self.game_unittest.board)

    def test_diagonal_unittest(self):
        print("Checking diagonal")
        self.game_unittest.board = ["X", "0", "X",
                                    " ", "X", "0",
                                    "0", "0", "X"]
        self.assertTrue(self.game_unittest.winner("X", 8))
        print(self.game_unittest.board)

    def other_conditions(self):
        print("None of checks are true")
        self.game_unittest.board = ["X", "0", "X"
                                    "0", "X", "0"
                                    "0", "X", " "]
        self.assertFalse(self.game_unittest.winner("X", 1))


if __name__ == "main":
    unittest.main()

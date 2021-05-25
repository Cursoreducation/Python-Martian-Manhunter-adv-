import unittest
from unittest.mock import patch
from game import TicTacToe


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()
        self.game.board[4] = "X"

    def test_available_moves(self):
        self.assertTrue(4 not in self.game.available_moves())

    def test_make_move(self):
        self.assertFalse(self.game.make_move(4, "X"))
        self.assertTrue(self.game.make_move(5, "X"))
        self.assertTrue(self.game.board[5] != " ")




    if __name__ == '__main__':
        unittest.main()

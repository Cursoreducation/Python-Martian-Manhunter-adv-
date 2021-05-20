import unittest
from game import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_winner(self):
        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']  # row
        self.assertTrue(self.game.winner(0, 'X'))
        self.assertTrue(self.game.winner(1, 'X'))
        self.assertTrue(self.game.winner(2, 'X'))
        self.assertTrue(self.game.winner(8, ' '))
        self.assertFalse(self.game.winner(5, '0'))

        self.game.board = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']  # row
        self.assertTrue(self.game.winner(3, 'X'))
        self.assertTrue(self.game.winner(4, 'X'))
        self.assertTrue(self.game.winner(5, 'X'))
        self.assertTrue(self.game.winner(8, ' '))
        self.assertFalse(self.game.winner(2, '0'))

        self.game.board = ['0', ' ', '0', ' ', ' ', ' ', 'X', 'X', 'X']  # row
        self.assertTrue(self.game.winner(6, 'X'))
        self.assertTrue(self.game.winner(7, 'X'))
        self.assertTrue(self.game.winner(8, 'X'))
        self.assertTrue(self.game.winner(3, ' '))
        self.assertFalse(self.game.winner(0, '0'))

        self.game.board = ['X', '0', '0', 'X', ' ', ' ', 'X', ' ', ' ']  # column
        self.assertTrue(self.game.winner(0, 'X'))
        self.assertTrue(self.game.winner(3, 'X'))
        self.assertTrue(self.game.winner(6, 'X'))
        self.assertFalse(self.game.winner(7, ' '))
        self.assertFalse(self.game.winner(4, '0'))

        self.game.board = ['0', 'X', ' ', ' ', 'X', ' ', ' ', 'X', '0']  # column
        self.assertTrue(self.game.winner(1, 'X'))
        self.assertTrue(self.game.winner(4, 'X'))
        self.assertTrue(self.game.winner(7, 'X'))
        self.assertFalse(self.game.winner(6, ' '))
        self.assertFalse(self.game.winner(3, '0'))

        self.game.board = [' ', '0', 'X', ' ', '0', 'X', ' ', ' ', 'X']  # column
        self.assertTrue(self.game.winner(2, 'X'))
        self.assertTrue(self.game.winner(5, 'X'))
        self.assertTrue(self.game.winner(8, 'X'))
        self.assertFalse(self.game.winner(7, ' '))
        self.assertFalse(self.game.winner(4, '0'))

        self.game.board = ['X', ' ', '0', ' ', 'X', ' ', '0', ' ', 'X']  # diagonal
        self.assertTrue(self.game.winner(0, 'X'))
        self.assertTrue(self.game.winner(4, 'X'))
        self.assertTrue(self.game.winner(8, 'X'))
        self.assertFalse(self.game.winner(1, ' '))
        self.assertFalse(self.game.winner(6, '0'))

        self.game.board = [' ', '0', 'X', ' ', 'X', ' ', 'X', ' ', '0']  # diagonal
        self.assertTrue(self.game.winner(2, 'X'))
        self.assertTrue(self.game.winner(4, 'X'))
        self.assertTrue(self.game.winner(6, 'X'))
        self.assertFalse(self.game.winner(0, ' '))
        self.assertFalse(self.game.winner(8, '0'))


if __name__ == "__main__":
    unittest.main()

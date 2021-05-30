import unittest
from game import TicTacToe


class TestWinner(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_winner_r(self):
        print('ROW')
        self.game.board = [' ', 'O', 'O', 'X', 'O', ' ', 'X', 'X', 'X']
        self.assertFalse(self.game.winner(2, 'O'))
        self.assertTrue(self.game.winner(8, 'X'))
        self.game.print_board()

    def test_winner_c(self):
        print("COLUMN")
        self.game.board = ['X', 'O', 'X', 'X', 'O', ' ', ' ', 'O', 'X']
        self.assertTrue(self.game.winner(4, 'O'))
        self.assertFalse(self.game.winner(0, 'O'))
        self.game.print_board()

    def test_winner_d(self):
        print('DIAGONAL')
        self.game.board = ['X', ' ', 'O', 'O', 'X', ' ', 'O', ' ', 'X']
        self.assertTrue(self.game.winner(8, 'X'))
        self.assertFalse(self.game.winner(5, 'X'))
        self.game.print_board()


if __name__ == '__main__':
    unittest.main()

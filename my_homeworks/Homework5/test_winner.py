import unittest
from game import TicTacToe


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_winner_by_raw(self):
        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=1, letter='X'), True)

        self.game.board = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=5, letter='X'), True)

        self.game.board = [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=8, letter='X'), True)

    def test_winner_by_diagonal(self):
        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=0, letter='X'), True)

        self.game.board = [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=6, letter='X'), True)

    def test_winner_by_column(self):
        self.game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=0, letter='X'), True)

        self.game.board = [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=1, letter='X'), True)

        self.game.board = [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=2, letter='X'), True)

    def test_not_win_by_raw(self):
        self.game.board = ['X', 'O', 'X', ' ', ' ', ' ', 'X', ' ', ' ']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=1, letter='X'), False)

        self.game.board = [' ', 'X', ' ', 'X', 'O', 'X', ' ', ' ', ' ']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=5, letter='X'), False)

        self.game.board = ['X', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'O']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=8, letter='X'), False)

    def test_not_win_by_diagonal(self):
        self.game.board = ['X', ' ', ' ', ' ', 'O', ' ', ' ', ' ', 'X']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=0, letter='X'), False)

        self.game.board = [' ', ' ', 'X', ' ', 'X', ' ', 'O', ' ', ' ']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=6, letter='X'), False)

    def test_not_win_by_column(self):
        self.game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'O', ' ', ' ']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=0, letter='X'), False)

        self.game.board = [' ', 'O', ' ', ' ', 'X', ' ', ' ', 'X', ' ']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=1, letter='X'), False)

        self.game.board = [' ', ' ', 'X', ' ', ' ', 'O', ' ', ' ', 'X']
        print(f'\n{self.game.board}')
        self.assertEqual(self.game.winner(square=2, letter='X'), False)


if __name__ == '__main__':

    unittest.main()

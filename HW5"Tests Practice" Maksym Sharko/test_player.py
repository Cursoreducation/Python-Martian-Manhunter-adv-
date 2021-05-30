import unittest
from unittest.mock import patch
from player import HumanPlayer, GeniusComputerPlayer
from game import TicTacToe


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()
        self.human_player = HumanPlayer("X")
        self.computer_player = GeniusComputerPlayer("O")

    @patch('player.input')
    @patch('game.TicTacToe.available_moves')
    def test_human_get_move(self, availableMovesMock, inputMock):
        inputMock.return_value = 4
        availableMovesMock.return_value = [0, 1, 3, 4, 5, 6, 7, 8]
        self.assertEqual(4, self.human_player.get_move(self.game))
        inputMock.return_value = 2
        self.assertIsNone(self.human_player.get_move(self.game))

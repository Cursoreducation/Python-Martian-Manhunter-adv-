from player import HumanPlayer, GeniusComputerPlayer
from game import TicTacToe

game = TicTacToe()
human_player = HumanPlayer("X")
computer_player = GeniusComputerPlayer("O")


def test_human_get_move(mocker):
    mocker.patch("player.input", return_value=4)
    mocker.patch("game.TicTacToe.available_moves", return_value=[0, 1, 3, 4, 5, 6, 7, 8])
    assert human_player.get_move(game) == 4

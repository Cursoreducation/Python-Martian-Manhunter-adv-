import pytest
from game import TicTacToe


def setup():
    global game_pytest
    game_pytest = TicTacToe()
    game_pytest.board[4] = "X"


def test_available_moves_pytest():
    assert 4 not in game_pytest.available_moves()


def test_make_move_pytest():
    assert not game_pytest.make_move(4, "X")
    assert game_pytest.make_move(5, "X")
    assert game_pytest.board[5] != " "

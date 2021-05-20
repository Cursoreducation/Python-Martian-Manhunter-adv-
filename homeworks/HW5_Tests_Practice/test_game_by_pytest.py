import pytest
from game import TicTacToe

game = TicTacToe()
game.board[4] = "X"


def test_available_moves():
    assert 4 not in game.available_moves()
    assert 3 in game.available_moves()
    assert 1 in game.available_moves()
    assert 8 in game.available_moves()
    with pytest.raises(AssertionError):
        assert 9 in game.available_moves()
        assert -1 in game.available_moves()


def test_make_move():
    assert game.make_move(4, "X") is False
    assert game.make_move(5, "X") is True
    with pytest.raises(IndexError):
        assert game.make_move(9, "X") is False
    assert game.board[5] != " "
    assert game.board[7] == " "

import pytest
from game import TicTacToe


@pytest.fixture
def return_tictactoe():
    return TicTacToe()


def setup():
    global game
    game = TicTacToe()
    game.board[4] = 'X'


def test_available_moves():
    assert 0 in game.available_moves()
    assert 3 in game.available_moves()
    assert -4 not in game.available_moves()
    assert 4 not in game.available_moves()
    with pytest.raises(AssertionError):
        assert -3 in game.available_moves()
        assert 9 in game.available_moves()


def test_make_move():
    assert not game.make_move(4, "X")
    assert game.make_move(5, "X")
    assert game.board[5] != ' '
    with pytest.raises(IndexError):
        assert game.make_move(9, "X") is False

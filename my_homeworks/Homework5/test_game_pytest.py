import pytest
from game import TicTacToe

game = TicTacToe()

game.board[3] = 'X'
game.board[7] = 'O'


def test_move_available():
    assert 3 not in game.available_moves()
    assert 7 not in game.available_moves()
    assert 4 in game.available_moves()


def test_make_move():
    assert game.make_move(square=6, letter='X') is True
    assert game.make_move(square=7, letter='X') is False
    assert game.make_move(square=3, letter='O') is False

    with pytest.raises(IndexError):
        assert game.make_move(9, 'X')

    with pytest.raises(TypeError):
        assert game.make_move(square='X', letter=2)
        assert game.make_move(square=3, letter=2)



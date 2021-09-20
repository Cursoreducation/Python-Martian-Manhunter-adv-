from game import TicTacToe

game = TicTacToe()
game.board[5] = 'X'
game.board[3] = 'O'


def test_available_moves_pytest():
    assert 4 in game.available_moves()
    assert 5 not in game.available_moves()


def test_make_move_pytest():
    assert game.make_move(4, 'X')
    assert not game.make_move(5, 'O')
    assert game.board[5] != " "

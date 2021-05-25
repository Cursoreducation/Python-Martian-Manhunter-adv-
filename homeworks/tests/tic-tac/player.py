import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

# RandomComputer & Human inherits, functions from the class Player with the super() keyword
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # computer makes a random choice out of the list of availabel moves remaining
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                # check to see if input is an integer or in the list of available moves
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square. Try again')
        return val

# This player use the minimax algorithm
class GeniusComputerPlayer(Player): 
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        print(square)
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = '0' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {
                'position:': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            }
        elif not state.empty_squares():
            return {
                'position': None,
                'score': 0
            }
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        for possible_move in state.available_moves():
            # make a move, and try that spot
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)
            # unod that move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # update the dictionaries
            # maximise the max_player
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            # minise the other_player
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
            
        return best
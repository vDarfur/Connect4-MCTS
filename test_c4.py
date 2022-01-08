#To use the test script, enter the amount of simulations for MCTS and 
#the number of games you would like MCTS to play against random as such

#./MCTS iterations games
#The output will be the agent's winning rate

#For 100 playouts and 100 iterations it should take about 1 minute 
#(I ran the simulation a couple times myself and it came out as 1.0 for 100 playouts on 100 iterations every time)

#If you would like to play against the agent, try 'pypy3 play_against.py numsimulations'. 1000 is a good number of simulations for a competitive agent

import random
import sys
import c4mcts
from connect4 import connect4



def random_choice(position):
    moves = position.legal_moves
    return random.choice(moves)


def compare_against_random(p1, games, initial_position):
    mcts_agent_wins = 0
    random_play_wins = 0 
    p1_strat = p1()
    draw = 0
    for i in range(games):
        position = initial_position

        while not position.game_over:
            if(position.player == 0):
                move = p1_strat(position)
                position = position.result(move)
            else:
                move = random.choice(position.legal_moves())
                position = position.result(move)
            
        if(position.winner == 0):
            mcts_agent_wins += 1
        else:
            draw += 1
    return mcts_agent_wins/games

def test_game():
    position = connect4()
    p1 = c4mcts.mcts_strategy
    iterations = int(sys.argv[1])
    games = int(sys.argv[2])
    win_pct = compare_against_random(lambda: p1(iterations),games, position)
    print(win_pct)


if __name__ == '__main__':
    test_game()

#Here you can play against an MCTS agent
#To run this program: 'pypy3 play_against.py numsimulations' where numsimulations is the amount of simulations you want the agent to do
#The agent will go first. To select your move, type the index of the column you would like to play
#Good Luck!

import random
import sys
import c4mcts
from connect4 import connect4

#plays against the agent
def play_against_agent(p1, initial_position):
    p1_strat = p1()
    draw = 0
    position = initial_position

    while not position.game_over:
        if(position.player == 0):
            move = p1_strat(position)
            position = position.result(move)
            for i in reversed(range(len(position.board))):
                print(" ".join(position.board[i]))
            print("")

        else:
            move = int(input())-1
            position = position.result(move)
            for i in reversed(range(len(position.board))):
                print(" ".join(position.board[i]))
            print("")

    exit(0)
       
def play():
    position = connect4()
    p1 = c4mcts.mcts_strategy
    play_against_agent(lambda: p1(int(sys.argv[1])), position)

if __name__ == '__main__':
    play()

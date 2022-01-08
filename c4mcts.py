import time
import random
from connect4 import connect4
import math
import copy
#initializing position object
class Node:
    def __init__(self, position):
        self.parent = None
        self.children = []
        self.position = position
        self.val = 0
        self.visits = 0
        self.move = 0

def mcts_strategy(iterations):
    playouts = 0
    
    #given the children of a node, return the index of the node to explore using UCB if player 1
    def player1Choice(children):
        maxIndex = 0
        maxVal = -100
        for i in range(len(children)):
            #if child has not been visited, the UCB is infinite so just return index
            if(children[i].visits == 0):
                maxIndex = i
                break
            #otherwise compute UCB
            childUCB = (children[i].val/children[i].visits)+(math.sqrt(2*(math.log(children[i].parent.visits))/children[i].visits))
            if(childUCB > maxVal):
                maxIndex = i
                maxVal = childUCB 
        return maxIndex

    #given the children of a node, return the index of the node to explore using UCB if player 2
    def player2Choice(children):
        maxIndex = 0
        maxVal = -100
        for i in range(len(children)):
            #if child has not been visited, the UCB is infinite so just return index
            if(children[i].visits == 0):
                maxIndex = i
                break
            #otherwise compute UCB
            childUCB = -(children[i].val/children[i].visits)+(math.sqrt(2*(math.log(children[i].parent.visits))/children[i].visits))
            if(childUCB > maxVal):
                maxIndex = i
                maxVal = childUCB
        return maxIndex
    #traverse the tree until we have found a leaf node

    def traverse(root):
        if(len(root.children) == 0):
            return root
        else:
            if(root.position.player == 0):
                exploreIndex = player1Choice(root.children)
            else:
                exploreIndex = player2Choice(root.children)
            return traverse(root.children[exploreIndex])
        
    def rollout(node):
        #first check if a position is game over
        if(node.position.game_over or node.visits == 0):
            return node
        else:
            legalMoves = node.position.legal_moves()
            for i in range(len(legalMoves)):
                newPos = node.position.result(legalMoves[i])
                newNode = Node(newPos)
                newNode.move = legalMoves[i]
                newNode.parent = node
                node.children.append(newNode)
            
        #return random child
        return random.choice(node.children)

    def simulate(node):
        currPos = copy.copy(node.position) #current position
        while(not currPos.game_over):
            move = random.choice(currPos.legal_moves())
            currPos = currPos.result(move)
        return currPos.winner

    #update stats back along path from leaf node
    def backpropogate(node, result):
        temp = node
        while(temp.parent):
            temp.visits += 1
            if(result == 0):
                temp.val+=1
            elif(result == 1):
                temp.val -=1
            temp = temp.parent 
        temp.val += 1
        temp.visits += 1
        return 
    
    def optimalMove(position):     
        #the root should be the original position we are given, from here grow the game tree
        root = Node(position)
        playouts = 0
        #driver loop
        while playouts < iterations:
            leaf = traverse(root)
            retNode = rollout(leaf)
            simResult = simulate(retNode)
            playouts+=1
            backpropogate(retNode, simResult)
        maxReward = 0
        minReward = 1000
        index = 0
        
        #finding the move that either optimizes or minimizes player 1 reward (optimize if p1, minimize if p2)
        if(root.position.player == 0):
            for i in range(len(root.children)):
                reward = root.children[i].val/root.children[i].visits
                if(reward > maxReward):
                    maxReward = reward
                    index = i
        else:
            for i in range(len(root.children)):
                reward = root.children[i].val/root.children[i].visits
                if(reward < minReward):
                    minReward = reward
                    index = i

        #return the move that's best
        return root.children[index].move

    return optimalMove

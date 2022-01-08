import copy
class connect4:
    def __init__(self):
        '''
            Creates a connect 4 board
            'x' represents an empty position
        '''
        self.height = 6
        self.width = 7
        self.board = [["x"]*7 for i in range(6)]
        self.heights = [0]*7
        self.player = 0
        self.game_over = False
        self.winner = -2
        
    def initial_position(self, s):
        '''Creates starting position for board 
        '''
        
    def legal_moves(self):
            '''Returns the legal moves from a given position
            '''
            legalMoves = []
            for i in range(len(self.heights)):
                if(self.heights[i] < 5):
                    legalMoves.append(i)
            return legalMoves
    
    def result(self, column): 
        '''Returns the position that results from placing a disk in a column
        '''
        height = self.heights[column]
        tempBoard = copy.deepcopy(self.board)
        if(self.player == 0):
            tempBoard[height][column] = "0"
        else:
            tempBoard[height][column] = "1"

        succ = connect4()
        succ.board = tempBoard
        succ.heights = copy.copy(self.heights)
        succ.heights[column] += 1
        succ.player = self.player

        if(succ.win(column)):
            succ.game_over = True
            succ.winner = self.player

        if(len(succ.legal_moves()) == 0):
            succ.game_over = True

        if(self.player == 0):
            succ.player = 1
        else:
            succ.player = 0
        
        return succ

    def board_full(self):
        '''Indicates whether or not the board is full
        '''
        #if the board is full, the game is over
        full = True
        for i in range(len(self.heights)):
            if(self.heights[i] != 5):
                full = False
                break

        return full 
    
    def win(self, column):
        '''
        Returns the winning if there was a win after a specific move, otherwise return -1
        Input should be the column that was last played
        last_played is the player who last placed a piece
        '''
        last_played = str(self.player)
        height = self.heights[column]-1
        #check diagonal
        #ascending diagonal
        if(height <= 3 and height >= 1 and column >= 1 and column <= 4):
            if(self.board[height-1][column-1] == last_played and self.board[height+1][column+1]==last_played and self.board[height+2][column+2] == last_played):
                return True
        
        if(height >= 2 and height <= 4 and column >= 2 and column <= 5):
            if(self.board[height-2][column-2] == last_played and self.board[height-1][column-1]==last_played and self.board[height+1][column+1] == last_played):
                return True
        
        if(height >= 3 and column >= 3):
            if(self.board[height-3][column-3] == last_played and self.board[height-2][column-2]==last_played and self.board[height-1][column-1] == last_played):
                return True
        if(height <=2 and column <=3):
            if(self.board[height+1][column+1] == last_played and self.board[height+2][column+2]==last_played and self.board[height+3][column+3] == last_played):
                return True

        #descending diagonal
        if(height >= 3 and column <= 3):
            if(self.board[height-1][column+1] == last_played and self.board[height-2][column+2]==last_played and self.board[height-3][column+3] == last_played):
                return True

        if(height >= 2 and height <= 4 and column >= 1 and column <= 4):
            if(self.board[height+1][column-1] == last_played and self.board[height-1][column+1] == last_played and self.board[height-2][column+2] == last_played):
                return True
        
        if(height >= 1 and height <= 3 and column >= 2 and column <= 5):
            if(self.board[height+1][column-1] == last_played and self.board[height+2][column-2] == last_played and self.board[height-1][column+1] == last_played):
                return True

        if(height <= 2 and column >= 3):
            if(self.board[height+1][column-1] == last_played and self.board[height+2][column-2] == last_played and self.board[height+3][column-3] == last_played):
                return True     
        #check horizontal
        if(column <= 3):
            if(self.board[height][column+1] == last_played and self.board[height][column+2] == last_played and self.board[height][column+3] == last_played):
                return True
        if(column >= 1 and column <= 4):
            if(self.board[height][column-1] == last_played and self.board[height][column+1] == last_played and self.board[height][column+2] == last_played):
                return True 
        if(column >= 2 and column <= 5):
            if(self.board[height][column-2] == last_played and self.board[height][column-1] == last_played and self.board[height][column+1] == last_played):
                return True
        if(column >= 3):
            if(self.board[height][column-1] == last_played and self.board[height][column-2] == last_played and self.board[height][column-3] == last_played):
                return True    
        #check vertical 
        if(height <= 2):
            if(self.board[height+1][column] == last_played and self.board[height+2][column] == last_played and self.board[height+3][column] == last_played):
                return True
        if(height >= 1 and height <= 3):
            if(self.board[height-1][column] == last_played and self.board[height+1][column] == last_played and self.board[height+2][column] == last_played):
                return True
        if(height >= 2 and height <= 4):
            if(self.board[height-2][column] == last_played and self.board[height-1][column] == last_played and self.board[height+1][column] == last_played):
                return True
        if(height >= 3):
            if(self.board[height-1][column] == last_played and self.board[height-2][column] == last_played and self.board[height-3][column] == last_played):
                return True
        return False
               

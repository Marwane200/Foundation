class Game:
    def __init__(self,player1,player2): 
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.move = 0

    def playGame(self):
   
        currPlayer = self.player1
        currToken = 1
        while not self.board.getWinner():

            if self.move % 2:
                currPlayer = self.player2
                currToken = -1
            else:
                currPlayer = self.player1
                currToken = 1

            self.playTurn(currPlayer,currToken)            
            self.move+=1
        
        winner = None 
        if self.board.getWinner() > 0:
            winner = self.player1
        else:
            winner = self.player2
        
        print(winner, " Wins!")
        self.board.printBoard()
        
    def playTurn(self,player,token):
        print(player,'\'s Turn')
        self.board.printBoard()
        try:
            row = int(input(" Select a row: "))
            col = int(input(" Select a col: "))
            self.board.placeToken(row,col,token)
        except Exception as e :
            print('Error: ', e)
            print('Please Try Again...')
            self.playTurn(player,token)

class Board:
    def __init__(self):
        self.board = [ ['#'] * 3 for row in range(3)]
        self.winRow = [ 0 for row in range(3)]
        self.winCol = [ 0 for row in range(3)]
        self.winDiag = [ 0 for row in range(2)]
        self.winner = 0

    def getWinner(self):
        return self.winner

    def printBoard(self):

        print('        col   ')
        print('row  0   1   2')
        
        for i in range(3):
            print(i,': ',self.board[i][0],'|',self.board[i][1],'|',self.board[i][2])
            if i < 2: print('     ---------')

    
    def placeToken(self, rowVal,colVal,token: int):

        row = int(rowVal)
        col = int(colVal)
        if row > 2 or row < 0: raise ValueError(f'Row {row}  is out of range!')
        if col > 2 or col < 0: raise ValueError(f'Col {col} out of range!')
        if self.board[row][col] != '#': raise ValueError('Token has been taken!')

        chip = '#' 
        if token > 0: chip = 'X'
        elif token < 0: chip = 'O'

         
        self.board[row][col] = chip

        self.winRow[row] += token
        self.winCol[col] += token
        if row == col: self.winDiag[0] += token 
        if row == 2 - col: self.winDiag[1] += token

        scores = [self.winRow[row], self.winCol[col], self.winDiag[0], self.winDiag[1]]
        for score in scores:
            if abs(score) == 3: self.winner = token


game = Game('Abdul','Mohammed')
print('Lets play tic tac toe')
game.playGame()


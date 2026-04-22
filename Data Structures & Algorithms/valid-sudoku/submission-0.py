class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each row - possibly a hash map, if a value is already there -> false
        for row in board:
            if not self.checkRow(row):
                return False
        
        #check each column - same as row
        for i in range(9):
            new_col = [
                board[0][i], board[1][i], board[2][i], 
                board[3][i], board[4][i], board[5][i], 
                board[6][i], board[7][i], board[8][i]
                ]
            if not self.checkRow(new_col):
                return False

        #check each 3x3 - first three, next three, last three
        for row in board:
            print(row)
        for i in range(3):
            for j in range(3):
                new_box = [
                    board[i*3][j*3], board[i*3][j*3+1], board[i*3][j*3+2],
                    board[i*3+1][j*3], board[i*3+1][j*3+1], board[i*3+1][j*3+2],
                    board[i*3+2][j*3], board[i*3+2][j*3+1], board[i*3+2][j*3+2]
                ]
                print('3x3 -> ', new_box)
                if not self.checkRow(new_box):
                    return False
        return True

    
    def checkRow(self, row: List[str]) -> bool:
        row_dict = dict()
        for x in row:
            if x != "." and x in row_dict:
                return False
            elif x != "." and x not in row_dict:
                row_dict[x] = 1
        return True
            
import time

start = time.time()

class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            
            l = [k for k in board[i] if not (k == '.')]
            #s = set(l)
            if not (len(set(l)) == len(l)):
                print("Row ",i," is not good")
                return False
            
            l = [k[i] for k in board if not (k[i] == '.')]
            #s = set(l)
            if not (len(set(l)) == len(l)):
                print("Column ",i," is not good")
                return False

            k = (i//3)*3
            h = (i%3)*3
            l = board[k][h:h+3] + board[k+1][h:h+3] + board[k+2][h:h+3]
            l = [k for k in l if not (k == '.')]
            #s = set(l)
            if not (len(set(l)) == len(l)):
                print("Regtangular ",i," is not good")
                return False
        return True
    
input1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

input2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

h = Solution()
print(h.isValidSudoku(input1))
print(h.isValidSudoku(input2))

end = time.time()
print(end - start)
        

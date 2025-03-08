# N Queen problum

def Nqueen(N):
    def is_safe(board,row,col):
        for i in range(col):
            if board[row][i]==1:
                return False
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if board[i][j]==1:
                return False
        for i,j in zip(range(row,N,1),range(col,-1,-1)):
            if board[i][j]==1:
                    return False
            return True
    def solve(board,col):
        if col>=N:
            return True
        for i in range(N):
            if is_safe(board,i,col):
                board[i][col]=1
                if solve(board,col+1):
                    return True
                board[i][col]=0
        return False
    board = [[0 for _ in range (N)] for _ in range (N)]
    if solve(board,0):
        for row in board:
            print(' '.join(str(x) for x in row))
    else:
        print("Solution does not exit ")

N = 8
Nqueen(N)



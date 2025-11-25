N,W,H = map(int,input().split())
matrix = []
dx=[1,0,-1,0]
dy=[0,1,0,-1]

for i in range(H):
    matrix.append(list(map(int,input().split())))

print(matrix)

def pop(a,b,n):
    for r in range(4):
        for k in range(n):
            x_move = a + k*dx[r]
            y_move = b + k*dy[r]

            if 0<=x_move<H and 0 <= y_move< W:
                matrix[a][b] = 0
                pop(x_move,y_move,matrix[x_move][y_move])
    



for m in range(H):
    for n in range(W):
        if matrix[m][n] != 0:
            pop(m,n,matrix[m][n])
            print(matrix)
          

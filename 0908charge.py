
def dir(num):
    global x_move,y_move
    if num == 0:
        x_move = x_move
        y_move = y_move
    
    if num == 1:
        x_move += dx[2]
        y_move += dy[2]
    
    if num == 2:
        x_move += dx[1]
        y_move += dy[1]

    if num == 3:
        x_move += dx[0]
        y_move += dy[0]

    if num == 4:
        x_move += dx[3]
        y_move += dy[3]

    return x_move,y_move

matrix = [[0]*10 for _ in range(10)]


def space(a,b,c,p):
    matrix[a-1][b-1] = p
    for k in range(4):
        x_c = a-1 + c*dx[k]
        y_c = b-1 + c*dy[k]

        if 0<=x_c<10 and 0<=y_c<10:
            matrix[x_c][y_c] = p


    


M,N = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

a_move = list(map(int,input().split()))
b_move = list(map(int,input().split()))

for k in range(N):
    A,B,C,P = map(int,input().split())
    space(A,B,C,P)
    

x_move,y_move = 0,0

for i in a_move:
    a_x, a_y= dir(i)


x_move,y_move = 9,9

for j in b_move:
    a_x,a_y = dir(j)

print(matrix)
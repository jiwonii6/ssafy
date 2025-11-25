T= int(input())

for tc in range(T):

    N= int(input())

    matrix = [list(map(int,input().split())) for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                drag_x = i
                drag_y = j
                break


    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    # k = 0
    # n = 0
    # nx = drag_x + dx[k] * n
    # ny = drag_y +dy[k] * n
    matrix[drag_x][drag_y] == 1
    n = 0

    while True: 

        for k in range(4):
            if 0 <= drag_x + dx[k] < N and 0 <= drag_y+dy[k]< N:
                if matrix[drag_x + n*dx[k]][drag_y+n*dy[k]] != 1:
                    matrix[drag_x + dx[k]][drag_y+dy[k]] = 1 -matrix[drag_x + dx[k]][drag_y+dy[k]]
            

                if matrix[drag_x + dx[k]][drag_y+dy[k]] == 1:
                    break

            drag_x = drag_x + dx[k]
            drag_y = drag_y+dy[k]


    print(matrix)
            


            



for m in range(N):
    for n in range(N):
        if matrix[m][n] == 0:
            count += 1

print(f'#{tc+1} {count}')

       

        


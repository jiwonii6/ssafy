T = int(input())

for tc in range(T):
    N= int(input())

    matrix = [list(map(int,input().split())) for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                drag_x = i
                drag_y = j
                break

    


    count = 0
    for m in range(N):
        for n in range(N):
            if matrix[m][n] == 0:
                count += 1
    print(matrix)
    print(f'#{tc+1} {count}')


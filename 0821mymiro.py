T = int(input())

for tc in range(T):
    N = int(input())
    matrix = []

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for i in range(N):
        numlist = list(map(int,input()))
        matrix.append(numlist)

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                que = [[i,j]]
                break

    count = 0
    visited = [[0]*N for _ in range(N)]

    flag = False

    while que:
        count += 1

        for _ in range(len(que)):
            qnum = que.pop(0)

            for k in range(4):
                x_move = qnum[0] + dx[k]
                y_move = qnum[1] + dy[k]

                if 0<=x_move<N and 0<=y_move<N and matrix[x_move][y_move] == 3:
                    flag = True
                    break


                if 0<=x_move<N and 0<=y_move<N and matrix[x_move][y_move] == 0 and visited[x_move][y_move] != 1:
                    visited[x_move][y_move] = 1
                    que.append([x_move,y_move])
                    # print(que)


        
        if flag:
            print(f'#{tc+1} {count-1}')
            break

    else:
        print(f'#{tc+1} 0')

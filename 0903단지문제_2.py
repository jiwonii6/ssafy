from collections import deque

N =int(input())

matrix = [list(map(int,input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

que = deque([])
list_count = []

for i in range(N):
    for j in range(N):

        if matrix[i][j] == 1 and visited[i][j] == 0:
            que.append((i,j))
            visited[i][j] = 1
            count = 1
            # print('aaaaaaaaaa')
            
            while que:
                print(que)
                nx,ny = que.popleft()

                for r in range(4):
                    x_move = nx + dx[r]
                    y_move = ny + dy[r]

                    if 0 <= x_move < N and 0 <= y_move<N:

                        if matrix[x_move][y_move] == 1 and visited[x_move][y_move] == 0 :
                            visited[x_move][y_move] = 1
                            que.append((x_move,y_move))
                            count += 1

            list_count.append(count)
            
            



result = sorted(list_count)

print(len(result))
for i in result:
    print(i)
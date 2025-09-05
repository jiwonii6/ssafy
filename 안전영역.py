from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N = int(input())

matrix = [list(map(int,input().split())) for _ in range(N)]
all_list = []

for i in range(N):
    for j in range(N):
        all_list.append(matrix[i][j])

num_list = list(set(all_list))

max_count = 0
que = deque([])

for r in num_list:
    new_matrix = [[0]*N for _ in range(N)]
    for m in range(N):
        for n in range(N):
            if r >= matrix[m][n]:
                new_matrix[m][n] = 1
            else:
                new_matrix[m][n] = 0

    visited = [[0]*N for _ in range(N)]
    que = deque([])

    if len(num_list) == 1:
        count = 1

    # print(new_matrix)
    count = 0 
    for p in range(N):
        for q in range(N):
            if new_matrix[p][q] == 0 and visited[p][q] == 0:
                que.append((p,q))
                visited[p][q] = 1
                count += 1
                while que:
                    # print(que)
                    nx,ny = que.popleft()

                    for k in range(4):
                        x_move = nx+dx[k]
                        y_move = ny+dy[k]

                        if 0<=x_move< N and 0<=y_move<N and new_matrix[x_move][y_move] == 0 and visited[x_move][y_move] == 0:
                            visited[x_move][y_move] = 1
                            que.append((x_move,y_move))
    
    # print(count)
    if max_count <= count:
        max_count = count


print(max_count)




# for i in range(N):
#     for j in range(N):
#         count = 0
#         visited = [[0]*N for _ in range(N)]
#         que.append((i,j))

#         while que:
#             nx,ny = que.popleft()
#             count += 1
#             visited[nx][ny] = 1

#             for r in range(4):
#                 x_move = nx + dx[r]
#                 y_move = ny + dy[r]

#                 if 0 <= x_move < N and 0 <= y_move < N:
#                     if matrix[i][j] >= matrix[x_move][y_move] and visited[x_move][y_move] == 0:
#                         visited[x_move][y_move] = 1
#                         que.append((x_move,y_move))

#         print(visited)

        


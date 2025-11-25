N,M = map(int,input().split())

matrix = [list(map(int,input())) for _ in range(N)]

q = [[0,0]]
visited = [[0]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

count = 0
flag = False

while q:
    count += 1
        
    for _ in range(len(q)):
        x_c,y_c = q.pop(0)
        for i in range(4):
            x_move = x_c + dx[i]
            y_move = y_c + dy[i]

            if x_move == N-1 and y_move == M-1: #끝에 도착했을때 바로 break
                    count += 1 
                    flag = True
                    break

            if 0 <= x_move < N and 0 <= y_move < M and visited[x_move][y_move] != 1 and matrix[x_move][y_move] == 1:
                q.append([x_move,y_move])
                visited[x_move][y_move] = 1
           
        if flag:
            break
    if flag:
        break


print(count)


# 다른 코드
from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

q = deque()
q.append((0, 0))
count = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    count += 1
    for _ in range(len(q)):
        x_c, y_c = q.popleft()

        # ✅ 도착점에 도달했는지 꺼내자마자 확인
        if x_c == N - 1 and y_c == M - 1:
            print(count)
            exit()

        for i in range(4):
            x_move = x_c + dx[i]
            y_move = y_c + dy[i]

            if 0 <= x_move < N and 0 <= y_move < M:
                if matrix[x_move][y_move] == 1 and not visited[x_move][y_move]:
                    visited[x_move][y_move] = 1
                    q.append((x_move, y_move))

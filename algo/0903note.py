from collections import deque

for tc in range(10):
    input()
    matrix = [list(map(int,input())) for _ in range(16)]

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    visited = [[0]*16 for _ in range(16)]
    x_cor,y_cor = 1,1



    def bfs(x,y):

        que =deque([(x,y)])
        visited[x][y] = 1

        while que:

            x_move,y_move = que.popleft()
            if matrix[x_move][y_move] == 3:
                return 1
            

            for i in range(4):
                nx = x_move + dx[i]
                ny = y_move + dy[i]
                if 0<= nx < 16 and 0 <= ny < 16 and matrix[nx][ny] != 1 and visited[nx][ny] != 1:
                    visited[nx][ny] = 1
                    que.append((nx,ny))

        return 0


    print(f'#{tc+1} {bfs(x_cor,y_cor)}')
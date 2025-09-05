import sys
sys.setrecursionlimit(2500)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# j가 행, i가 열
def dfs(i,j):
    global count

    if [i,j] in new_list and visited[i][j] == 0:
        count = 1
        visited[i][j] = 1

    for r in range(4):
        y_move = j + dy[r]
        x_move = i + dx[r]
        if 0 <= x_move < N and 0 <= y_move < M:
            if [x_move,y_move] in new_list and visited[x_move][y_move] == 0:
                visited[x_move][y_move] = 1
                count += 1
                dfs(x_move,y_move)



T= int(input())

for tc in range(T):

    N,M,K = map(int,input().split())

    visited = [[0]*M for _ in range(N)]

    new_list = []

    result = 0

    for _ in range(K):
        new_list.append(list(map(int,input().split())))

    for k in new_list:
        count = 0
        dfs(k[0],k[1])
        if count:
            result += 1


    print(result)



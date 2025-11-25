def bfs(i,j): # 2차원 배열 만들기
    visited = [[0] * 16 for _ in range(16)]
    q = [[i,j]]
    visited[i][j] = 1
    flag = False
    while q:
        ti,tj = q.pop(0)
        if maze[ti][tj] == 3: 
            flag = True
            print(f'#{tc+1} 1')
            break

        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi,wj = ti+di, tj+dj
            if 0 <= wi < 16 and 0<= wj < 16 and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi,wj])
                visited[wi][wj] = visited[ti][tj] + 1


    if not flag:
        print(f'#{tc+1} 0')
            
for tc in range(10):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    sti,stj = 1,1
    ans = bfs(sti,stj)
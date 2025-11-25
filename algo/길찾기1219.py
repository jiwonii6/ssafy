T= 10

def dfs(node):
    global answer

    visited[node] = 1

    if node == 99:
        answer = 1
        return
    
    for next_node in adj_list[node]:

        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)

for tc in range(1,T+1):
    _,M = map(int,input().split())
    info = list(map(int,input().split()))
    adj_list = [[] for _ in range(100)]
    answer = 0
    visited = [0]*100

    for i in range(M):
        a = info[2*i]
        b = info[2*i + 1]

        adj_list[a].append(b)

    visited[0] = 1
    dfs(0)
    visited[0] = 0

    


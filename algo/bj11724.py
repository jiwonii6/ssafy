# from collections import deque

# N,M = map(int,input().split())
# graph = [[] for _ in range(N+1)]
# visited = [0]*(N+1)
# count = 0

# def bfs(num):
#     que = deque([num])
#     visited[num] = 1
#     while que:
#         current = que.popleft()
#         for k in graph[current]:
#             if visited[k] == 0:
#                 que.append(k)
#                 visited[k] = 1

# for i in range(M):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)


# for r in range(1,N+1):
#     if visited[r] == 0:
#         bfs(r)
#         count += 1

# print(count)


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
count = 0

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)


def dfs(num):
    stack = [num]
    visited[num] = 1
    result = []
    while stack:
        current = stack.pop()
        result.append(current)
        for i in graph[current]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
    return result
        


for k in range(1,N+1):
    if visited[k] == 0:
        dfs(k)
        count += 1
    
print(count)

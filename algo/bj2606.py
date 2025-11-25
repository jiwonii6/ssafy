# N = int(input())
# M = int(input())
# total = []
# for i in range(M):
#     a,b = map(int,input().split())
#     total.append([a,b])
    

# # print(total)

# visited = [[0,0] for _ in range(M)]

# result = [1]
# real = []


# while result:
#     p = result.pop()
#     for j in range(M):
#         for r in range(2):
#             if p in total[j] and visited[j][r] == 0:
#                 visited[j][r] = 1 
#                 result.append(total[j][r])
#                 real.append(total[j][r])
#                 print(result)


# answer = len(set(real))

# if not real:
#     print(0)
# else:
#     print(answer-1)

from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

visited = [0] *(N+1)
total = []

def bfs(start):
    que = deque([start])
    visited[start] = 1
    while que:
        current = que.popleft()
        total.append(current)
        for num in graph[current]:
            if visited[num] == 0:
                visited[num] = 1
                que.append(num)


        
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    

bfs(1)
print(len(total)-1)
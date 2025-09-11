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

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

visited = [0] *(N+1)
total = [1]

print(visited)
print(graph)

def bfs(current):
    current = total.pop()
    if visited[current] == 0:
        for num in graph[current]:
            visited[num] = 1
            total.append(num)
            bfs(num)
            

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    



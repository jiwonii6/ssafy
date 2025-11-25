
from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

def find(i,j):
    global count
    que = deque([(i,j,count)])
    visited[i][j] = 1
    
    count_list = []
    while que:
        # print(que)
        a,b,count = que.popleft()
  
        if matrix[a][b] == 2:
            count_list.append(count)
     
        for r in range(4):
                x_move = a + dx[r]
                y_move = b + dy[r]
                if 0 <= x_move < N and 0 <= y_move < N and visited[x_move][y_move] == 0:
                    que.append((x_move,y_move,count+1))
                    visited[x_move][y_move] = 1

    return count_list
    
                
result = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            visited = [[0]*N for _ in range(N)]
            count = 0
            result.append(find(i,j))

            
print(result)


# from itertools import combinations
# N, M = map(int,input().split())
# graph = [[0]*N for _ in range(N)]

# home_rcs = []
# store_rcs = []
# answer = float('inf')

# for r in range(N):
#     row =list(map(int,input().split()))
#     for c in range(N):
#         graph[r][c] = row[c]

#         if graph[r][c] ==1:
#             home_rcs.append((r,c))
#         elif graph[r][c] == 2:
#             store_rcs.append((r,c))

# distances = [[0]*len(store_rcs) for _ in range(len(home_rcs))]

# for home_idx in range(len(home_rcs)):
#     for store_idx in range(len(store_rcs)):

#         distances[home_idx][store_idx] = abs(home_rcs[home_idx][0]-store_rcs[store_idx][0])+abs(home_rcs[home_idx][1]-store_rcs[store_idx][1])



# for store_idx_set in combinations(range(len(store_rcs)), M): # --> 박스 하나를 그때그떄만 사용하고 말아서 메모리 효율적이다.
#     distance = 0
#     for home_idx in range(len(home_rcs)):
#         min_distance = 2*(N-1)
#         for store_idx in store_idx_set:
#             min_distance = min(min_distance,distances[home_idx][store_idx])

#         distance += min_distance

#     answer = min(answer,distance)

# print(answer)
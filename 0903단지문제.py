def dfs(i,j):
    global count

    for r in range(4):
        x_move = i +dx[r]
        y_move = j + dy[r]

        # if x_move >= N or x_move < 0 or y_move >= N or y_move <0 or matrix[x_move][y_move] == 0:
        #     continue

        if 0<=x_move<N and 0<=y_move<N and matrix[x_move][y_move] == 1 and visited[x_move][y_move] == 0:
            count += 1
            visited[x_move][y_move] = 1
            dfs(x_move,y_move)
        
        
N = int(input())

matrix = [list(map(int,input())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


visited = [[0]*N for _ in range(N)]
count_total = []

for i in range(N):
    for j in range(N):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                count = 1
                # print(i,j)
                dfs(i,j)
                count_total.append(count)


sort_total = sorted(count_total)

print(len(count_total))
for k in sort_total:
     print(k)
            

                
                # print(count)




# 승준님 풀이

# def dfs_house(r, c, temp_answer):
#     if house_map[r][c] == 0: return
#     for move_r, move_c in move_d :
#         now_r = r + move_r
#         now_c = c + move_c
#         if now_r<0 or now_r >= N or now_c <0 or now_c>=N : continue
#         if visited[now_r][now_c] : continue
#         if house_map[now_r][now_c] == 1 :
#             visited[now_r][now_c] = 1
#             temp_answer += 1
#             temp_answer = dfs_house(now_r, now_c, temp_answer)
#     return temp_answer



# N = int(input())
# house_map = [list(map(int, input())) for _ in range(N)]
# visited = [[0]*N for _ in range(N)]

# # 상하좌우
# move_d = [[-1,0], [1,0], [0,-1], [0, 1]]

# house_complex = []

# for i in range(N) :
#     for j in range(N) :

#         # 지도 내 값이 0이면 건너뛰기
#         if house_map[i][j] == 0 : continue
#         # 방문한 적이 있으면 건너뛰기
#         ## house_map이 0이든 1이든 상관없이
#         if visited[i][j] : continue
#         visited[i][j] = 1
#         temp_answer = dfs_house(i, j, 1)
#         if temp_answer != 0 :
#             house_complex.append(temp_answer)

# complex_cnt = len(house_complex)
# house_complex.sort()
# print(complex_cnt)
# for i in range(complex_cnt) :
#     print(house_complex[i])
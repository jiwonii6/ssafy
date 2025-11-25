
# for tc in range(10):
#     input()
#     matrix = []

#     for i in range(100):
#         row = list(map(int,input().split()))
#         matrix.append(row)

#         if i == 99:
#             y = row.index(2)

#         x = 99
        
#     while x > 0:
#         if y - 1 >= 0 and matrix[x][y - 1] == 1:
#             y -= 1
#             # print(f'{x},{y}')
#             matrix[x][y] = False

#         elif y + 1 >= 0 and y+1 <=99  and matrix[x][y + 1] == 1:
#             y += 1
#             # print(f'{x},{y}')
#             matrix[x][y] = False
            

#         elif x - 1 >= 0 and matrix[x - 1][y] == 1:
#             x -= 1
#             # print(f'{x},{y}')
#             matrix[x][y] = False

#         else:
#             break

#     print(f'#{tc} {y}')

# for tc in range(10):
#     input()
    
#     matrix = [list(map(int,input().split())) for _ in range(100)]
    
#     for ind in range(100):
#         if matrix[99][ind]== 2:
#             y = ind

#     x = 99
        
#     while x > 0:
#         if y - 1 >= 0 and matrix[x][y - 1] == 1:
#             y -= 1
#             # print(f'{x},{y}')
#             matrix[x][y] = False

#         elif y + 1 >= 0 and y+1 <=99  and matrix[x][y + 1] == 1:
#             y += 1
#             # print(f'{x},{y}')
#             matrix[x][y] = False
            

#         elif x - 1 >= 0 and matrix[x - 1][y] == 1:
#             x -= 1
#             # print(f'{x},{y}')
#             matrix[x][y] = False

#         else:
#             break

#     print(f'#{tc} {y}')


# 0 : 상, 1: 좌, 2: 우
dr = [-1,0,0]
dc = [0,-1,1]

# 0 : [1,2,0]
# 1 : [0,1]
# 2 : [0,2]

search_dir = [[1,2,0],[0,1],[0,2]]

T = 10
for tc in range(1,T+1):
    input()
    ladder = [list(map(int,input().split())) for _ in range(100) ]
    r = 99
    c = ladder[99].index(2)

    dir = 0
    while r > 0 :

        # 다음 방향 탐색
        for i in range(len(search_dir[dir])):
            # 다음 방향 후보
            next_dir = search_dir[dir][i]
            next_r = r+dr[next_dir]
            next_c = c+dc(next_dir)

            if 0 <= next_c < 100 and ladder[next_r][next_c] == 1:
                dir = next_dir
                r = next_r
                c = next_c
                break


    print(f'{tc} {c}')



matrix = [list(map(int,input())) for _ in range(16)]

for tc in range(10):

    p = [[1,1]]

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    visited = [[0]*16 for _ in range(16)]

    flag = False

    while p:
        for _ in range(len(p)):
            x_c,y_c = p.pop(0)

            for r in range(4):
                x_move = x_c + dx[r]
                y_move = y_c + dy[r]

                # if x_move <0 or x_move >= 16 or y_move <0 or y_move >= 16 or matrix[x_move][y_move] == 1 or visited[x_move][y_move] == 1:
                #     continue
                if 0<=x_move<16 and 0 <=y_move <16 and matrix[x_move][y_move] == 0 and visited[x_move][y_move] == 0:
                        p.append([x_move,y_move])
                        visited[x_move][y_move] = 1


            if flag: 
                print(f'#{tc+1} 1')
                break

        else:
            print(f'#{tc+1} 0')

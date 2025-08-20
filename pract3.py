N= int(input())

for tc in range(N):

    matrix = []
    box = []
    result_list = []

    for i in range(9):
        row = list(map(int,input().split()))
        matrix.append(row)
    # print(matrix)


    for k in range(9):
        col = []
        col_list = []
        for l in range(9):
            col.append(matrix[l][k])
        
        matrix.append(col)
        


    for k in range(0,9,3):
        for h in range(0,9,3):
            box = []
            for i in range(0,3):
                for j in range(0,3):
                    box.append(matrix[i+k][j+h])

            matrix.append(box)



    # for num in range(9):
    #     if set(matrix[num]) != set([1,2,3,4,5,6,7,8,9]) or set(col_list[num]) != set([1,2,3,4,5,6,7,8,9])  or set(result_list[num]) != set([1,2,3,4,5,6,7,8,9]):
    #         print(f"#{tc+1} 0")
    #         break

    # else:
    #             print(f'#{tc+1} 1')

    for num in range(27):
        if set(matrix[num]) != set([1,2,3,4,5,6,7,8,9]):
            print(f"#{tc+1} 0")
            break

    else:
        print(f'#{tc+1} 1')


    # flag = False
    # for i in range(9):
    #     visited = set()
    #     for j in range(9):
    #         before_len = len(visited)
    #         visited.add(matrix[i][j])
    #         after_len = len(visited)

    #         if before_len == after_len:
    #             flag = True
    #             break
    #             # 여긴 중복

    # if not flag:
    #     for i in range(9):
    #         visited = set()
    #         for j in range(9):
    #             before_len = len(visited)
    #             visited.add(matrix[j][i])
    #             after_len = len(visited)

    #             if before_len == after_len:
    #                 flag = True
    #                 break

    # if not flag:

T = int(input())

for tc in range(T):
    N,M = map(int,input().split())

    matrix = [list(map(int,input())) for _ in range(N)]


    def cor(x,y):
        for i in range(x):
            for j in range(y-1,0,-1):
                if matrix[i][j] == 1:
                    return i,j

    x_cor,y_cor = cor(N,M)

    i = x_cor
    code_list = []
    count = 0

    while count <= 7:
        new_list = []
        for j in range(7):
            new_list.append(matrix[i][y_cor-j])
        y_cor = y_cor - 7

        code_list.append(new_list)
        count += 1
    result_list = []

    for k in range(7,-1,-1):
        a = code_list[k][::-1]

        if a == [0,0,0,1,1,0,1]:
            result_list.append(0)
            

        elif a == [0,0,1,1,0,0,1]:
            result_list.append(1)

        elif a == [0,0,1,0,0,1,1]:
            result_list.append(2)

        elif a == [0,1,1,1,1,0,1]:
            result_list.append(3)

        elif a == [0,1,0,0,0,1,1]:
            result_list.append(4)

        elif a == [0,1,1,0,0,0,1]:
            result_list.append(5)

        elif a == [0,1,0,1,1,1,1]:
            result_list.append(6)

        elif a == [0,1,1,1,0,1,1]:
            result_list.append(7)

        elif a == [0,1,1,0,1,1,1]:
            result_list.append(8)

        elif a == [0,0,0,1,0,1,1]:
            result_list.append(9)


    odd = 0
    even = 0

    for i in range(8):
        if (i+1) % 2 == 1:
            odd += result_list[i]
        else:
            even += result_list[i]

    if (odd*3 + even) % 10 == 0:
        print(f'#{tc+1} {odd+even}')
    else:
        print(f'#{tc+1} 0')
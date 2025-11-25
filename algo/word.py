tc = int(input())

for num in range(tc):
    N,M = list(map(int,input().split()))

    matrix = [list(map(int,input().split())) for _ in range(N)]


    print(matrix)

    col_total = []

    for k in range(N):
        col_list = []
        for j in range(N):
            col_list.append(matrix[j][k])

        col_total.append(col_list)

    print(col_total)


    count = 0

    for row in matrix: 
        for j in range(N-M):

            if j == 0 and row[:j+M+1] == [1]*M +[0]:
                count += 1
                print(f'a {count}')

            elif j == N-(M+1) and row[N-(M+1):] == [0] + [1]*M:
                count += 1
                print(f'b {count}')
            

            elif row[j:j+M+2] ==[0]+[1]*M+[0]:
                count += 1
                print(f'c {count}')

    for col in col_total:
        for i in range(N-M):

            if i == 0 and col[:i+M+1] == [1]*M +[0]:
                count += 1 
                print(f'd {count}')
                
            elif i == N-(M+1) and col[N-(M+1):] == [0] + [1]*M :
                count += 1
                print(f'e {count}')
                
                
            elif col[i:i+M+2] == [0]+[1]*M+[0]:
                count += 1
                print(f'f {count}')


    print(f'#{num+1} {count}')


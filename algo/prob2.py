N = int(input())

for i in range(N):

    a,b = list(map(int,input().split()))
    matrix = [list(map(int,input().split())) for _ in range(a)]
    sum_list = []


    for m in range(a-b+1):
        for n in range(a-b+1):
            sum = 0
            for x in range(b):
                for y in range(b):
                    sum += matrix[m+x][n+y]

            
            sum_list.append(sum)


    print(f'{i+1} {max(sum_list)}')

                



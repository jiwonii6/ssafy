for tc in range(10):
    num = int(input())
    matrix = [list(input()) for _ in range(8)]
    cols = [list (a) for a in zip(*matrix)]

    count =0 
    for i in matrix:
        for j in range(9-num):
            rand_list = i[j:j+num]
            if rand_list == rand_list[::-1]:
                count += 1

    for k in cols:
        for r in range(9-num):
            rand_col = k[r:r+num]
            if rand_col == rand_col[::-1]:
                count += 1


    print(f'#{tc+1} {count}')
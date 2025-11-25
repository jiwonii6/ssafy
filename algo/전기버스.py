K,N,M = map(int,input().split())

stat = list(map(int,input().split()))

x_move = 0

count = 0

for j in stat:
    if x_move <= M:
        x_move += K
        print(f'{x_move} a')
        print(j)
        if x_move >= j:
            count += 1
        else:
            break


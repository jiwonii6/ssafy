T = int(input())

for tc in range(1,T+1):
    candy = list(map(int,input().split()))
    count = 0
    for i in range(len(candy)-2,-1,-1):
        if candy[i] >= candy[i+1]:
            while candy[i] >= candy[i+1]:
                candy[i] -= 1
                count += 1


        if candy[i] <= 0:
            count = -1
            break

    print(f'#{tc} {count}')
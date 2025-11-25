T= int(input())

for tc in range(1,T+1):
    N = int(input())
    numlist = list(map(int,input().split()))

    heap = [0] * (N+1)
    last = 0 


    for i in numlist:
        last += 1 
        heap[last] = i

        c =last
        p = c // 2 
        while p and heap[p] > heap[c]: 
            heap[p],heap[c] = heap[c],heap[p]
            c = p
            p = c // 2

    index = N

    result = 0

    while index > 1:
        index = index // 2 
        result += heap[index]
        
    print(f'#{tc} {result}')

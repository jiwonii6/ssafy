T = int(input())

for tc in range(1, T+1):

    N = int(input())

    num_list = list(map(int, input().split()))

    # idx: 현재 위치를 나타내는 변수
    # count: 총 수행 횟수
    # count_stop: 최대 갈 수 있는 인덱스 
    idx = 0
    count = 0

    for i in range(1, N):
        # 1. i 지점으로 최초 이동
        # 2. i 지점에서 되돌아가라고 하는 곳까지 이동
        # 3. i 지점까지 원복
        # count_stop += 1

        if i == 1:
            idx = num_list[i-1] 
        
        else:

            idx = num_list[i-1] - 1


        # 만약 되돌아갔다면 현 위치를 가장 멀리 갔던 곳(count_stop)까지 이동
        # while idx <= count_stop:
        while idx < i:
            count += 1  
            idx += 1

        if i == N-1:
            break  

        count +=1


    
        
        # count += 1




    
    print(f'#{tc} {count}')

# T = int(input())
# for tc in range(T):
#     N = int(input())

#     num_list = list(map(int,input().split()))

#     move = 0
#     count = 0

#     for i in range(1,len(num_list)):
#         if i == 1:
#             move = i - (num_list[i-1])
#             count += move

#         else:
#             move = i - (num_list[i-1]-1)
#             count += move

#         if i == N-1:
#             break
        

#         count +=1


#     print(f' #{tc+1} {count}')
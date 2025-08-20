# T = int(input())

# for tc in range(T):
#     N = int(input())

#     num_list = list(map(int,input()))

#     max_count = 0
#     count = 0

#     for i in range(N):
#         if num_list[i] == 1:
#             count += 1

#         else:
#             count = 0

#         if max_count < count:
#             max_count = count

#     print(f'#{tc+1} {max_count}')
    
T = int(input())

for tc in range(T):
    N = int(input())

    num_list = list(map(int,input()))

    max_count = 0
    count = 0
    
    flag = False

    for i in range(N):
        if num_list[i] == 1:
            count += 1
            flag = False

        if max_count < count:
            max_count = count

        if num_list[i] == 0:
            flag = True

    if flag:
        count = 0

    

    print(f'# {tc+1} {max_count}')
    


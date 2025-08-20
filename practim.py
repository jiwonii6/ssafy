# tc = int(input())

# for num in range(tc):
#     num,diff = map(int,input().split())

#     power = list(map(int,input().split()))
#     sort_power = sorted(power) #정렬

#     max_count = 1 # 가장 큰 그룹 크기를 저장할 변수  

#     for i in range(num-1):
#         count = 1
#         for j in range(i+1,num): #i 이후의 값들과 비교
#             if sort_power[i] + diff >= sort_power[j]: #차이가 diff 이하면 count 증가
#                 count += 1 

#         if max_count < count:
#             max_count = count


#     print(max_count) # count는 i 이후 값 개수만 세므로 자기 자신을 포함하려면 +1

# 야구 선수 문제
# 3
# 4 2
# 6 4 2 3
# 4 3
# 1 2 3 4
# 4 1
# 1 3 7 5

# 강사님 풀이

# T = int(input())

# for tc in range(1,T+1):
#     N,K = map(int,input().split())
#     stats = list(map(int,input().split()))

#     answer =  1
    
#     stats.sort()

#     for i in range(N-1): 
#         temp = 1
#         for j in range(j+1,N):
#             if stats[j] - stats[i] > K:
#                 break

#             temp += 1 #else 안적어도 됨. 왜냐면 조건 만족하면 break돼서 안옴.

#         answer = max(answer,temp)

#포인터 사용

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    stats = list(map(int,input().split()))

    answer =  1
    
    stats.sort()

    left = 0
    right = 0 #0,1 상관 없음
     
    while right <=N:
        if stats[right] - stats[left] <= K:
            right += 1
            answer = max(answer,right-left)
            continue #else 필요 없어짐
        
        left += 1

    print(answer)


#회문

for tc in range(1,T+1):
    for j in range(8-N+1):

        for k in range(N//2):
            if graph[i][j+k] != graph[i][j+N-1-K]:
                break
    else:
        answer += 1 #위에 한번도 안 거쳤을 경우 바로 else로 for-else 구문


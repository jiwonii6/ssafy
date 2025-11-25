import math

def dfs(count,left,right):
    global answer

    if left >= total_weight / 2:
        answer += 2**(N-count)*math.factorial(N-count)
        return

    if count == N:
        answer += 1
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = 1
        dfs(count+1,left+weights[i],right)
        if right+weights[i] <= left:
            dfs(count+1,left,right+weights[i])
        visited[i] = 0



T = int(input())

for tc in range(1,T+1):
    answer = 0
    N = int(input())
    weights = list(map(int,input().split()))
    total_weight = sum(weights)
    visited = [0] * N

    dfs(0,0,0)
    print(f'{tc} {answer}')



# def dfs(count,diff):
#     global visited

#     if dp[visited].get(diff):
#         return dp[visited][diff]

#     if count == N:
#         dp[visited][diff] = 1
#         return dp[visited][diff]
#     case_count = 0

#     for i in range(N):
#         if visited & (1 << i): # and 연산
#             continue

#         visited |= (1 << i) # or 연산
#         dfs(count+1,diff+weights[i])
#         if diff-weights[i] >= 0:
#             case_count += dfs(count+1, diff-weights[i])
#         visited ^= (1 << i)

#     dp[visited][diff] = case_count
#     return case_count




# T = int(input())

# for tc in range(1,T+1):
#     answer = 0

#     N = int(input())
#     weights = list(map(int,input().split()))

#     dp= [{} for _ in range(2**9)] #2**9-1 이 나올수 있는 경우의 수?
#     visited = 0

#     anser = dfs()

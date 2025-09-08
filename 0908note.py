# name = ["MIN","CO","TIM"]
# path = []
# arr = ["O","X"]

# def recur(cnt):
#     #종료조건 (3명을 모두 고려)
#     if cnt == 3:
#         print(*path)
#         return 
    
#     # 재귀호출 파트
#     # - 부분집합에 포함 되는 경우(O를 추가)
#     path.append(arr[0])
#     recur(cnt+1)
#     path.pop()

#     # - 포함되지 않는 경우(X를 추가)
#     path.append(arr[1])
#     recur(cnt+1)
#     path.pop()
    

# recur(0)


# name = ["MIN","CO","TIM"]

# def recur(cnt,subset):
#     if cnt == 3:
#         print(*subset)
#         return
    
#     #부분집합에 포함 시키는 경우
#     recur(cnt+1, subset + [name[cnt]])
#     #포함 시키지 않는 경우
#     recur(cnt+1,subset)

# recur(0,[])

# MIN CO TIM
# MIN CO
# MIN TIM
# MIN
# CO TIM
# CO
# TIM

# arr = [1,2,3,4]

# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         if i & (1 << idx):
#             print(arr[idx], end = " ")
    
#     print()

# 1
# 2
# 1 2
# 3
# 1 3
# 2 3
# 1 2 3
# 4
# 1 4
# 2 4
# 1 2 4
# 3 4
# 1 3 4
# 2 3 4
# 1 2 3 4 


# arr = [1,2,3,4]
# # i: 0~2^n == i번째 부분집합

# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         if i & (1 << idx):
#             print(arr[idx],end = " ")

#     print()
# 0
# # arr = ['A','B','C']
# n = len(arr)

# def get_sub(tar):
#     print(f'target = {tar}', end=' / ')
#     for i in range(len(arr)):
#         if tar & 0x1:
#             print(arr[i], end = ' ')
#         tar >>= 1

# for target in range(1 << len(arr)):
#     get_sub(target)
#     print()

# for target in range(1 << n):
#     get_sub(target)
#     print()

    
# for target in range(len(arr)+1):
#     get_sub(target)
#     print()

# 1
# 2
# 1 2
# 3
# 1 3
# 2 3
# 1 2 3
# 4
# 1 4
# 2 4
# 1 2 4
# 3 4
# 1 3 4
# 2 3 4
# 1 2 3 4

# target = 0 /
# target = 1 / 1
# target = 2 / 2
# target = 3 / 1 2
# target = 4 / 3
# target = 5 / 1 3
# target = 6 / 2 3
# target = 7 / 1 2 3
# target = 8 / 4
# target = 9 / 1 4
# target = 10 / 2 4
# target = 11 / 1 2 4
# target = 12 / 3 4
# target = 13 / 1 3 4
# target = 14 / 2 3 4
# target = 15 / 1 2 3 4

arr = ['A','B','C','D','E']
N = 3
path = []

def recur(cnt,start):

    if cnt == N:
        print(*path)
        return
    
    for i in range(start,len(arr)):
        path.append(arr[i])
        recur(cnt+1,i) # i 번째를 골랐으니, 다음 선택은 i 부터 고려(중복을 허용하는 조합)
        # recur(cnt+1,i+1) # i 번째를 골랐으니, 다음 선택은 i+1 부터 고려(중복을 허용하지 않는 조합)
        path.pop()

recur(0,0)
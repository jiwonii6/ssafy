path = []
N = 3

def run(lev):
    if lev == N:
        print(path)
        return
    for i in range(1,4):
        path.append(i)
        run(lev+1)
        path.pop()

run(0)
#
#
# def KFC(x):
#     print(x)
#     x += 1
#     print(x)
#
# x = 3
# KFC(x+1)
# print(x)
#
# def BBQ(x):
#     x += 10
#     print(x)
#
# def KFC(x):
#     print(x)
#     x += 3
#     BBQ(x+2)
#     print(x)
#
# x = 3
# KFC(x+1)
# print(x)
#
# #파라미터 N : 누적값
# def KFC(n):
#     if n == 3: # 종료조건 항상 생각(기저조건 - base-case)
#         return
#
#     print(n, end=' ')
#     KFC(n+1)
#     print(n, end=' ')
#
# KFC(0) #어디서 출발할지.시작점 항상 생각

path = [] # used,visited --> 뽑은 카드들을 저장

#used = [False,False,False] #고를 수 있는 수 만큼 만들어준다
#used = [False] * N # N개의 카드 종류가 있는 경우
#
# used = [False] * 7
#
# def recur(cnt):
#     if cnt == 3:
#         print(*path)
#         return
#
#     for num in range(1,7):
#         if used[num]:
#             continue
#
#         used[num] = 1
#         path.append(num)
#         recur(cnt+1)
#         path.pop()
#         used[num] = 0 #초기화
#
#
# recur(0)

# 주사위 3개를 던져서 합이 10 이하의 케이스의 수

# 중복 순열

# path = [] # 무조건 기존 주사위를 기록해놔야할까?
# result = 0
#
# def recur(cnt,total):
#     global result
#
#     if total > 10:
#         return
#
#     if cnt == 3:
#         # if total <= 10: #여기까지만 생각해도 ㄱㅊ
#         #     result += 1
#         result += 1
#
#     for num in range(1,7):
#         recur(cnt+1,total+num)
#
# recur(0,0)
# print(result)
#
# cards = ['A','J','Q','K']
# path = []
# result = 0
#
# # 연속된 3개가 나오면 return TRUE, 아니면 FALSE
# def count_three():
#
#     if path[0] == path[1] == path[2]:
#         return True
#     if path[0] == path[1] == path[3]:
#         return True
#     if path[0] == path[1] == path[4]:
#         return True
#
#     return False
#
# def recur(cnt):
#     global result
#
#     if cnt == 5:
#         if count_three():
#             result += 1
#         # 연속된 3개가 나오면 counting 하도록 만들어야함 -> 함수 만들자
#         return
#
#     for idx in range(len(cards)):
#         path.append(cards[idx])
#         recur(cnt+1)
#         path.pop()
#
# recur(0)
# print(result)
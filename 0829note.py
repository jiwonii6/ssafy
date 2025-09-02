# '''
# 13 
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
# '''

# def pre_order(T):
#     if T > 0:
#         print(T,end = ' ') #visit(T)
#         pre_order(left[T])
#         pre_order(right[T])


# def in_order(T):
#     if T > 0:
#         in_order(left(T))
#         print(T,end = ' ') #visit(T)
#         in_order(right[T])

# def post_order(T):
#     if T > 0:
#         post_order(left[T])
#         post_order(right[T])
#         print(T,end = ' ') #visit(T)

        

# V = int(input())
# E = V - 1
# arr = list(map(int,input().split()))

# left = [0] * (V+1) # 부모번호를 인덱스로 자식번호 저장
# right = [0] * (V+1)
# par = [0] * (V+1) # 자식번호를 인덱스로 부모번호 저장

# for i in range(E):
#     p,c = arr[i*2],arr[i*2+1]
#     par[c] = p
#     if left[p] == 0:
#         left[p] = c
#     else:
#         right[p] = c

# root = 1
# for i in range(1,V+1):
#     if par[i] == 0: #부모 노드가 없는 경우
#         root = i
#         break

# pre_order(root)
# print()
# in_order()
# print()
# post_order(root)

# 힙 사용
heap = [0] * 100
last = 0 # 마지막 정점 번호


def enq(n):
    global last
    last += 1 # 마지막 정점 추가
    heap[last] = n

    c =last
    p = c // 2 # 완전이진트리 자식 -> 부호 번호 연산
    while p and heap[p] < heap[c]: #부모가 있고, 부모 < 자식, 키값 교환
        heap[p],heap[c] = heap[c],heap[p]
        c = p
        p = c // 2

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

print(heap)



def pre_order(T):
    if T == 0:
        return 0 
    l = pre_order(left[T])
    r = pre_order(right[T])
    return l + r + 1

E,N = map(int,input().split())
arr = list(map(int,input().split()))
V= E + 1
left = [0] * (V+1)
right = [0] * (V+1)

for i in range(E):
    p,c = arr[i*2],arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

cnt = 0
print(pre_order(N))

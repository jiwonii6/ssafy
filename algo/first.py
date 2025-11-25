# bit = [0,0,0,0]

# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)


# def print_subset(bit):
#     for i in range(4):
#         if bit[i]:
#             print(arr[i], end = ' ')
#     print(bit)


# arr = [3,6,7,1,5,4]
# count = 0
# n = len(arr)
# for i in range(1<<n):
#     for j in range(n):
#         # print(arr[j], end = ", ")
#         if i & (1<<j): 
#             #i 는 2진수로 나타낸 생태
#             #1 << j는 어디가 1로 되어있나 찾음
#             # i가 1 나오는 곳을 찾아서 인덱싱함 > 부분집합
#             print(arr[j], end=", ")

#     count += 1
#     print()
# print()

# print(count)

def binarySearch(a,N,key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key :
            return middle
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle +1

    return -1


#재귀함수 이용
def binarySearch2(a,low,high,key) :
    if low > high :
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle] :
            return True
        elif key < a[middle]:
            return binarySearch2(a,low,middle-1,key)
        elif a[middle] < key :
            return binarySearch2(a,middle+1,high,key)
        


#선택 정렬 알고리즘
def selection_sort(a,N):
    for i in range(N-1): #정렬 구간의 시작 인덱스
        min_idx = i #첫 원소를 최소로 가정
        for j in range(i+1,N):
            if a[min_idx] > a[j]: # 최소 원소 위치 갱신
                min_idx = j
        a[i],a[min_idx] = a[min_idx],a[i] # 구간 최솟값을 구간 맨 앞으로


# K번쨰로 작은 원소를 찾는 알고리즘

# def select(arr,k):
#     for i in range(0,k):
#         min_index = i
#         for j in range(i+1,len(arr)):
#             if arr[min_index] > arr[j] :
#                 min_index = j
#         arr[i],arr[min_index] = arr[min_index], arr[i]
#     return arr[k-1]


# N = 3
# numbers = [1,2,3]
# visited = [0]* N

# #재귀 0,1만 나옴

# def subset(count):
#     if count == N:
#         #visited 결정
#         print(visited)
#         return 
    
#     subset(count+1)
#     visited[count] = 1
#     subset(count+1)
#     visited[count] = 0

# subset(0)


N = 3
numbers = [1,2,3]
visited = [0]* N

#재귀 숫자 나옴
#처음에 공백 생김 
def subset(count):
    if count == N:
        #visited 결정
        for i in range(N):
            if visited[i]:
                print(numbers[i], end = " ")
        print()
        return 
    
    subset(count+1)
    visited[count] = 1
    subset(count+1)
    visited[count] = 0

subset(0)

# #순열 코드
# numbers = [1, 2, 3, 4, 5]
# picked_numbers = []
# M = 3
# visited = [0]*len(numbers)

# def perm(count):
#     if count == M:
#         print(picked_numbers)
#         return
    
#     for i in range(len(numbers)):
#         if visited[i] == 1:
#             continue
#         picked_numbers.append(numbers[i])
#         visited[i] = 1
#         perm(count+1)
#         picked_numbers.pop()
#         visited[i] = 0

# perm(0)

# # 조합 코드!
# # 조합은 순열과 달리 지금 위치 오른쪽만 뽑음
# numbers = [1, 2, 3, 4, 5]
# picked_numbers = []
# M = 3

# def comb(count,idx):
#     print(picked_numbers)
#     if count == M:
#         return
    
#     for i in range(idx,len(numbers)):
#         picked_numbers.append(numbers[i])
#         comb(count+1,i+1)
#         picked_numbers.pop()

# comb(0,0)


    
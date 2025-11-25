from collections import deque

for tc in range(10):
    a = int(input())
    queue = deque(list(map(int,input().split())))

    while queue[-1] > 0:
        for i in range(1,6):
            queue[0] -= i
            a = queue[0]
            queue.popleft()
            queue.append(a)
            if a <= 0:
                queue[-1] = 0
                break

    print(f'#{tc+1}', *queue)



# while queue[-1] > 0:
#     for i in range(1,6):
#         queue[0] -= i
#         a = queue[0]
#         queue.popleft()
#         queue.append(a)
#         if a <= 0:
#             queue[-1] = 0
#             break
    
# print(queue)


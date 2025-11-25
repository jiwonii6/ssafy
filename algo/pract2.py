# front = rear = -1
# q = [0] * 10

# rear += 1
# q[rear] =1
# rear += 1
# q[rear] = 2
# rear += 1
# q[rear] = 3

# front += 1
# print(q[front]) # 1
# front += 1
# print(q[front]) # 2
# front += 1
# print(q[front]) # 3

from collections import deque

deque_q = deque()

for i in range(1000000):
    deque_q.append(i)

for _ in range(1000000):
    deque_q.popleft()
print('end')

list_q = []
for i in range(1000000):
    list_q.append(i)
print('end')




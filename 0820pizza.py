from collections import deque

N,M = map(int,input().split())


cheeze_list = deque(map(int,input().split()))
pizza = deque([])
count = 0

for _ in range(N):
    pizza.append(cheeze_list[0])
    cheeze_list.popleft()


while True:
    for i in range(N):
        pizza[i] = pizza[i] // 2

        if cheeze_list:
            if pizza[i] == 0:
                count += 1
                pizza[i] = cheeze_list[0]
                cheeze_list.popleft()
   
    
    if not cheeze_list:
        print(pizza)
        break
            
    print(f'{pizza} pizza')



print(count)
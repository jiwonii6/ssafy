N = int(input())
total = []
sum = 0
matrix = [[0]*100 for _ in range(100)]
for i in range(N):
    a,b = map(int,input().split())
    total.append([a,b])

for k in range(N):
    for m in range(k+1,N):
        x_1,y_1 = total[k]
        x_2,y_2 = total[m]
        
        if abs(x_1-x_2) < 10 and abs(y_1-y_2) < 10:
                sum += (10 - abs(x_1-x_2))*(10 - abs(y_1-y_2))


answer = N*100 - sum

print(answer)
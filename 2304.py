N = int(input())
x = []
dict = {}
max_b = -1

for i in range(N):
    a,b = map(int,input().split())
    dict[a] = b
    x.append(a)
    if b > max_b:
        max_b = b
        max_a = a

new_list = []
x_sort = sorted(x)
x_index = x_sort.index(max_a)
for i in x_sort:
    new_list.append([i,dict[i]])

sum = 0
now_x = new_list[0][0]
now_y = new_list[0][1]
for m in range(1,x_index+1):
    if now_y <= new_list[m][1]:
        sum += now_y*(new_list[m][0] - now_x)
        now_x = new_list[m][0]
        now_y = new_list[m][1]

now_x = new_list[N-1][0]
now_y = new_list[N-1][1]
for m in range(N-1,x_index-1,-1):
    if now_y < new_list[m][1]:
        sum += now_y*(now_x-new_list[m][0])
        now_x = new_list[m][0]
        now_y = new_list[m][1]

sum += new_list[x_index][1]

print(sum)
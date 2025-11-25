stack = list(input())

print(stack)

for i in range(len(stack)): 
    for j in range(i,len(stack)):
        if stack[i] == '{':
            stack[i].pop()
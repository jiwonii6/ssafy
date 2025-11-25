arr = list(input())
new_list = []
stack = []

for i in arr:
    if i == '(' or i == ')' or i == '{' or i== '}':
        new_list.append(i)

# print(stack)

for i in range(len(new_list)):
    if new_list[i] == '(' or new_list[i] == '{':
        stack.append(new_list[i])

    if new_list[i] == ')':
        
#순열 코드!중복순열?
numbers = [1,2,3,4,5]
pick_numbers = []
M = 3
visited = [0]*len(numbers)

def perm():
    if count == M:
        print(pick_numbers)
        return
    
    for i in range(len(numbers)):
        if visited[i] == 1:
            continue
        pick_numbers.append(numbers[i])
        visited[i] = 1
        perm(count+1)
        pick_numbers.pop()
        visited[i] = 0


perm(0)


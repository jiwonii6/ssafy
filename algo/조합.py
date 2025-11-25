N = 2
numbers = [1,2,3,4]
pick_numbers = []

def comb(count,idx):
    # print(pick_numbers)

    if count == N:
        # print(pick_numbers)
        return
    
    for i in range(idx,len(numbers)):
        pick_numbers.append(numbers[i])
        comb(count+1,i+1)
        pick_numbers.pop()

comb(0,0)

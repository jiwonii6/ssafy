switch_num = int(input())

switch = list(map(int,input().split()))

num =  int(input())

change = [list(map(int,input().split())) for _ in range(num)]

flag= False
for i in range(num):
    for j in range(len(switch)):
        if change[i][0] == 1:
            if (j+1) % change[i][1] == 0:
                switch[j] = 1- switch[j]

        
        else:
            switch_copy = switch[:]
            m = change[i][1] - 1
            for r in range(len(switch)):
                if switch_copy[m+r] != switch_copy[m-r] or m+r >= len(switch) or m-r < 0:
                    flag = True
                    break

                else:
                    if r ==0:
                        switch[m+r] = 1- switch[m+r] 

                    else:
                        switch[m+r] = 1- switch[m+r] 
                        switch[m-r] = 1 - switch[m-r]
                        print(switch)


            if flag:
                break

    if flag:
        break

# count = 0
# for num in switch:
#     print(num, end = ' ')
#     count += 1
#     if count % 20 == 0:
#         print()


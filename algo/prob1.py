for _ in range(10):

    tc_num = int(input())

    matrix = []
    col_list = []
    max_list = []


    for _ in range(100):
        row = list(map(int,input().split()))
        matrix.append(row)
        max_list.append(max(row))
        
        
    for k in range(100):
        list1 = []
        for i in matrix:
            list1.append(i[k])
        max_list.append(max(list1))



    print(max_list)




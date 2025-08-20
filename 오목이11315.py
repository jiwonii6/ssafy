T= int(input())

for tc in range(T):
    
    N = int(input())

    matrix = [list(input()) for _ in range(N)]
    cols = [list(col) for col in zip(*matrix)]
    flag = False

    while True:
        for i in matrix:
            count = 0
            for j in range(len(i)):
                if i[j] == 'o':
                    count += 1
                    if count == 5:
                        flag = True
                        break
                else:
                    count = 0

        for m in cols:
            count = 0
            for n in range(len(m)):
                if m[n] == 'o':
                    count += 1
                    if count == 5:
                        flag = True
                        break
                else:
                    count = 0

        for i in range(N):
            for j in range(N):
                diag_count = 0
                count = 0
                
                for k in range(5):
                    if 0<= i+k < N and 0 <= j-k <N:
                        if matrix[i+k][j-k] == 'o':
                            diag_count += 1
                            if diag_count == 5:
                                flag = True
                                break
                        else: 
                            break

                for r in range(5):
                    if 0<= i+r < N and 0 <= j+r < N:
                        if matrix[i+r][j+r] == 'o':
                            count += 1
                            if count == 5:
                                flag = True
                                break
                        else:
                            break


        if flag:
            print(f"#{tc+1} YES")
            break
        else:
            print(f"#{tc+1} NO")
            break

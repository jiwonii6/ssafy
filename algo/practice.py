def fibo(n):
    global cnt
    cnt += 1
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
def fibo1(n):
    global cnt1
    cnt1 += 1
    if n>= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]


cnt = 0
print(fibo(10),cnt)

memo = [0] * 11
memo[0] = 0
memo[1] = 1
cnt1 = 0
print(fibo1(10),cnt1)


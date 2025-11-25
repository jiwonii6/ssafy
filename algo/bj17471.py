from collections import deque

N = int(input())
ppl = list(map(int,input().split()))
graph = [[]]

num_ppl = list(range(1,N+1))


empty = []

def dfs(graph_A,graph_B):
    
    que_A =deque(graph_A)
    que_B = deque(graph_B)

    while que_A:

        p = que_A.popleft()

        


    

for k in range(N):
    new_list = list(map(int,input().split()))
    new_list.pop(0)
    graph.append(new_list)


print(graph)

def comb(idx,count,n):

    if count == n:
        a_list = empty
        b_list = list(set(num_ppl) - set(a_list))

        print(a_list,b_list)


    for j in range(idx,N):
        empty.append(num_ppl[j])
        comb(j+1,count+1,n)
        empty.pop()


for i in range(N):
    visited = [0] * (N+1)
    adj = list(map(int,input().split()))
    comb(0,0,i)

    

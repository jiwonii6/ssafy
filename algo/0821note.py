def bfs(s,V):
    #초기화
    # visited 생성
    # 큐 생성
    # 시작점 인큐
    # 시작점 인큐표시
    # 반복

    #초기화
    visited = [0] * (V+1) #visited 생성
    q = [s] # 큐 생성
            # 시작점 인큐 
    visited[s] = 1 # 시작점 인큐표시
    #반복
    while q: # 탐색할 정점이 남아 있으면
        t = q.pop(0) #디큐
        print(t) # visit(), 방문정점 출력
        for w in adj_lst[t] : # t번행에 감. 인접하고 미방문인 정점 인큐, 인큐표시
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1





V,E = map(int,input().split()) # 마지막 정점, 간선 수

arr = list(map(int,input().split()))

adj_lst =[[] for _ in range(V+1)] # V번행까지 준비

for i in range(E):
    v1,v2 = arr[i*2], arr[i*2+1]
    adj_lst[v1].append(v2) #v1 -> v2 (방향표시가 없는 경우)
    adj_lst[v2].append(v1) #v2 -> v1 (양방향 이동 가능) 


bfs(1,V) # 1번부터 V번까지 출발점은 1
print()
bfs(4,V) # 출발점이 4


# 다른 방식
# for i in range(0,E*2,2):
#     v1,v2 = arr[i],arr[i+1]
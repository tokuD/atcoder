import heapq
N,M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    u,v,c = map(int, input().split())
    G[u].append([v,c])

INF = 10**15
#* minutes[n]:街nまでの最短時間
minutes = [INF]*N
minutes[0] = 0

visited = [False]*N

#* heapq [minutes,city]
Q = []
heapq.heappush(Q, [0,0])
#* ダイクストラ法
while len(Q)>0:
    m,c = heapq.heappop(Q)
    if visited[c]:
        continue
    visited[c] = True
    for nex,time in G[c]:
        minutes[nex] = min(minutes[nex],minutes[c]+time)
        heapq.heappush(Q, [minutes[nex],nex])

print(minutes[-1])
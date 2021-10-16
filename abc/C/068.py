import heapq
N,M = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

#* 頂点0から各頂点までの最短距離
dist = [-1]*N

visited = [False]*N
#* ヒープ
Q = []

heapq.heappush(Q, [0,0])
dist[0] = 0

while len(Q) > 0:
    dis,now = heapq.heappop(Q)
    if visited[now]:
        continue
    visited[now] = True
    for n in G[now]:
        x = 1
        if dist[n] == -1 or dist[n] > dis + x:
            dist[n] = dis + x
            heapq.heappush(Q, [dist[n],n])

if dist[N-1] == 2:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
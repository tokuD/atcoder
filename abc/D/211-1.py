from collections import deque
N,M = map(int, input().split())
G = [[] for _ in range(M)]
for _ in range(M):
    a,b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

#* 都市0からの距離ごとにグループ分け
#* distance[i]:都市0からの距離が0のグループ
distance = [[] for _ in range(N)]

Q = deque()
Q.append([0,0])
visited = [False]*N
while len(Q) > 0:
    curr, depth = Q.popleft()

    if visited[curr]:
        continue

    visited[curr] = True
    distance[depth].append(curr)

    for nxt in G[curr]:
        Q.append([nxt,depth+1])

#* dp[i]:最短距離で都市iまで何通りか
dp = [0]*N
dp[0] = 1
for dis in range(N):
    for i in distance[dis]:
        
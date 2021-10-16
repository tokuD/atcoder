N,M = map(int, input().split())
INF = 10**20
#* G[i][j]:街iから街jに何分かかるか
G = [[INF]*N for _ in range(N)]
for i in range(N):
    G[i][i] = 0

for i in range(M):
    u,v,c = map(int, input().split())
    G[u][v] = min(G[u][v],c)



for k in range(N):
    for x in range(N):
        for y in range(N):
            G[x][y] = min(G[x][y],G[x][k]+G[k][y])

ans = 0

for i in range(N):
    ans += sum(G[i])

print(ans)
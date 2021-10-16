import heapq
N,M = map(int, input().split())
G = [[] for _ in range(N)]
ans = 0
for _ in range(M):
    u,v,c = map(int, input().split())
    G[u].append((c,v))
    G[v].append((c,u))

#* heapq
Q = []

visited = [False]*N
visited_count = 0

visited[0] = True
visited_count += 1

#* 街0からの道をheapに入れる
for cost,next_city in G[0]:
    heapq.heappush(Q, (cost,next_city))

while visited_count < N:
    cost,next_city = heapq.heappop(Q)
    if visited[next_city]:
        continue
    visited[next_city] = True
    visited_count += 1
    ans += cost

    #* 今訪れた街から作れる道をheapに追加
    for c,n in G[next_city]:
        if visited[n]:
            continue
        heapq.heappush(Q, (c,n))

print(ans)
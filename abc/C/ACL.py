from collections import deque
N,M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    a,b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)


visited = [False]*N
#* ある都市から行ける都市を幅優先探索
def bfs(n):
    global visited
    Q = deque()
    Q.append(n)
    while len(Q) > 0:
        now_city = Q.popleft()
        visited[now_city] = True

        #* 今の都市から行ける都市を探索
        for next_city in G[now_city]:

            #* 訪問済ならスキップ
            if visited[next_city]:
                continue

            #* まだ行っていないなら探索予定を追加
            Q.append(next_city)

ans = -1

#* 各都市からスタートしてbfsし、グループ数を計算
for i in range(N):

    #* 探索済ならスキップ
    if visited[i]:
        continue

    #* 未探索なら ans += 1 してbfs
    ans += 1
    bfs(i)

print(ans)
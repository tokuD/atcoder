import sys
sys.setrecursionlimit(10**7)
N,M = map(int, input().split())
#* G[i]:都市iから行ける都市
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
ans = 0
def dfs(i):

    #* 訪問済の場合スキップ
    if visited[i]:
        return

    #* 訪問チェック&カウント
    visited[i] = True
    global ans
    ans += 1

    #* 今いる都市iから行ける都市を探す
    for nxt in G[i]:
        dfs(nxt)



#* 各都市についてdfsで通れる都市を数える
#* 計算量はO(N*N)
for i in range(N):
    #* スタート地点が都市iの場合
    visited = [False]*N
    dfs(i)

print(ans)
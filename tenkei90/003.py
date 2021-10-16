import sys
sys.setrecursionlimit(10**6)
N = int(input())
#* G[i]:都市iから行ける都市
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

depthes = [0]*N
visited = [False]*N
def dfs(n,depth):
    """ある頂点からの深さを探索"""

    #* 来ていたら終了
    if visited[n]:
        return

    #* チェックを入れる
    visited[n] = True

    #* 深さをメモ
    depthes[n] = depth

    #* 都市nからいける都市を探索
    for i in G[n]:
        dfs(i,depth+1)

#* 都市0から最も遠い都市uを探す
depthes = [0]*N
visited = [False]*N
dfs(0,0)
u = 0
l = 0
for i in range(N):
    if l < depthes[i]:
        l = depthes[i]
        u = i

#* 都市uから最も遠い都市vまでの距離を求める
depthes = [0]*N
visited = [False]*N
dfs(u,0)

print(max(depthes)+1)

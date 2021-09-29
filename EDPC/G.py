import sys
sys.setrecursionlimit(10**7)

N,M = map(int,input().split())
#* graph[i]=[j,k,l]:頂点iから頂点[j,k,l]に向かって辺が張られている
graph = [[] for _ in range(N+1)]
parents = [[] for _ in range(N+1)]
for i in range(1,M+1):
    x,y = map(int, input().split())
    graph[x].append(y)
    parents[y].append(x)


#* start地点の候補(根)
root = []
for i in range(1,N+1):
    if len(parents[i]) == 0:
        root.append(i)

def dfs(par,depth):
    """頂点iから葉までの距離を求める"""

    #* 子を持たない場合
    if len(graph[par]) == 0:
        return depth

    #* 子を持つ場合
    l = 0
    for chi in graph[par]:
        l = max(l,dfs(chi,depth+1))
    return l

ans = 0
for i in root:
    ans = max(ans,dfs(i,0))

print(ans)

import sys
sys.setrecursionlimit(10**7)
import heapq
N = int(input())
G = [[] for _ in range(N)]

for i in range(N-1):
    a,b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(N):
    G[i].sort()

ans = []

visited = [False]*N
visited[0] = True
#* dfs(今いる都市,前いた都市)
def dfs(i,j):

    #* 訪れた都市を出力
    ans.append(str(i+1))

    #* visitedにチェック
    visited[i] = True

    #* heapqから番号が小さい順に取り出し
    for next_city in G[i]:
        #* 未訪問なら行く
        if not visited[next_city]:
            dfs(next_city,i)

    #* 行けるとこは全部行った＆今いる都市が0の場合
    if i == 0:
        return

    #* 行けるとこは全部行った＆今いる都市が0じゃない場合
    else:
        ans.append(str(j+1))
        return

dfs(0,0)

print(' '.join(ans))
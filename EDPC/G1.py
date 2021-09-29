import sys
sys.setrecursionlimit(10**6)

N,M = map(int, input().split())
children = [[] for _ in range(N+1)] #* graph[i]:頂点iの子
parents = [[] for _ in range(N+1)] #* parents[i]:頂点iの親

for i in range(1,M+1):
    x,y = map(int,input().split())
    children[x].append(y)
    parents[y].append(x)

#* 頂点iからのpathの最大値
length = [0] * (N+1)

#* length[i]が既に計算済みかどうか
done = [False] * (N+1)

def rec(i):

    #* 計算済みの場合
    if done[i]:
        return length[i]

    for j in children[i]:
        length[i] = max(length[i], rec(j)+1)

    done[i] = True
    return length[i]

ans = 0
for i in range(1,N+1):
    if len(parents[i]) == 0:
        ans = max(ans,rec(i))

print(ans)

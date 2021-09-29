import sys
sys.setrecursionlimit(10**6)
H,W = map(int,input().split())
C = [list(input()) for _ in  range(H)]
s = []
g = []
visited = [[False]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if C[i][j] == 's':
            s = [i,j]
            s.append(j)
        if C[i][j] == 'g':
            g = [i,j]

def dfs(h,w):

    #探索済みに変更
    visited[h][w] = True

    #上下左右を探索
    for i,j in [[h+1,w],[h-1,w],[h,w+1],[h,w-1]]:

        #はみ出す場合はスキップ
        if not (0<=i<H and 0<=j<W):
            continue

        #塀の場合はスキップ
        if C[i][j] == '#':
            continue

        #探索済みの場合スキップ
        if visited[i][j]:
            continue

        #再帰呼び出し
        dfs(i,j)

dfs(s[0],s[1])

if visited[g[0]][g[1]]:
    print('Yes')
else:
    print('No')
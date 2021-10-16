from collections import deque
N,q = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

#* odd[i]:街iが、街0から数えて偶数番目かどうか
odd = [False]*N

#* 幅優先探索
Q = deque()
#* Q=[街,深さ]
Q.append([0,0])
visited = [False]*N
while len(Q)>0:
    curr, depth = Q.popleft()

    #* 訪問済ならスキップ
    if visited[curr]:
        continue

    #* 訪問したことをチェック
    visited[curr] = True

    #* 深さが偶数ならoddを更新
    if depth % 2 == 0:
        odd[curr] = True

    #* 繋がっている街を訪問予約
    for nxt in G[curr]:
        Q.append([nxt,depth+1])

#* 偶偶、奇奇ならTown
ans = []
for _ in range(q):
    c,d = map(lambda x:int(x)-1, input().split())
    if odd[c] ^ odd[d]:
        ans.append('Road')
    else:
        ans.append('Town')

for a in ans:
    print(a)
from collections import deque
N,M = map(int, input().split())
G = [[] for _ in range(N)]
mod = 10**9+7

for i in range(M):
    a,b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

INF = 10**10
#* depth[i]:[都市iまでの深さ,通り数]
depth = [[INF,0] for _ in range(N)]
depth[0][1] = 1
Q = deque()
#* [都市,深さ,どこから来たか]
Q.append([0,0,0])

#* bfs
while len(Q) > 0:
    curr, d, pre = Q.popleft()

    #* 以前の行き方の方が近いならスキップ
    if depth[curr][0] < d:
        continue

    #* 以前の行き方と同じ距離なら足す
    if depth[curr][0] == d:
        depth[curr][1] += depth[pre][1]
        depth[curr][1] %= mod
        continue

    #* 以前の行き方より近い場合
    if d < depth[curr][0]:
        depth[curr][0] = d
        depth[curr][1] = depth[pre][1]
        depth[curr][1] %= mod

    # print(depth)
    # print(curr+1,d,pre+1)
    #* 次に行ける都市を探索
    for nxt in G[curr]:
        Q.append([nxt,d+1,curr])

print(depth[-1][1] % mod)
# print(depth)
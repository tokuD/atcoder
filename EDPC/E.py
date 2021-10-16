N,weight = map(int, input().split())
W = []
V = []
for _ in range(N):
    w,v = map(int, input().split())
    W.append(w)
    V.append(v)
v_total = sum(V)
INF = 10**12
dp = [[INF]*(v_total+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(v_total+1):
        if dp[i][j] == INF:
            continue

        #* 選ばない場合
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])

        #* 選ぶ場合
        dp[i+1][j+V[i]] = min(dp[i+1][j+V[i]],dp[i][j]+W[i])

for i in range(v_total+1)[::-1]:
    w = dp[-1][i]
    if w <= weight:
        print(i)
        break

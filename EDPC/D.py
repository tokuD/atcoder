N,W = map(int,input().split())
WV = [list(map(int,input().split())) for _ in range(N)]

dp = [[-1]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(W):
        if dp[i][j] == -1:
            continue
        dp[i+1][j] = max(dp[i+1][j],dp[i][j])
        if j+WV[i][0] <= W:
            dp[i+1][j+WV[i][0]] = max(dp[i+1][j+WV[i][0]],dp[i][j]+WV[i][1])

ans = 0
for i in range(1,W+1):
    ans = max(ans,dp[-1][i])

print(ans)
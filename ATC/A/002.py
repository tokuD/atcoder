N = int(input())
P = list(map(int,input().split()))
M = 100 * N
dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(M):
        if not dp[i][j]:
            continue
        dp[i+1][j] = True
        if j+P[i]<=M:
            dp[i+1][j+P[i]] = True

print(sum(dp[-1]))
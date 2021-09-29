N = int(input())
A = list(map(int, input().split()))
mod = 998244353

dp = [[[0]*10 for i in range(10)] for _ in range(N)]
dp[0][A[0]][A[1]] = 1

for i in range(N-1):
    for j in range(10):
        for k in range(10):
            if dp[i][j][k] == 0:
                continue

            #* 操作Fの場合
            f0 = (j+k) % 10
            if i+2 < N:
                f1 = A[i+2]
                dp[i+1][f0][f1] += dp[i][j][k]
                dp[i+1][f0][f1] %= mod
            else:
                dp[i+1][f0][0] += dp[i][j][k]
                dp[i+1][f0][0] %= mod

            #* 操作Gの場合
            g0 = (j*k) % 10
            if i+2 < N:
                g1 = A[i+2]
                dp[i+1][g0][g1] += dp[i][j][k]
                dp[i+1][g0][g1] %= mod
            else:
                dp[i+1][g0][0] += dp[i][j][k]
                dp[i+1][g0][0] %= mod

for i in range(10):
    print(dp[-1][i][0])
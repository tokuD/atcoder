mod = 998244353
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

dp = [[0]*(B[-1]+1) for _ in range(N+1)]
dp[0][0] = 1

#* 配るdp
for i in range(N):
    for j in range(B[-1]+1):
        if dp[i][j] == 0:
            continue

        #* 使える数字の範囲
        mi,ma = A[i],B[i]

        #* 下に渡す
        if mi <= j <= ma:
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod

        #* 右に渡す
        if j+1<=B[-1]:
            dp[i][j+1] += dp[i][j]
            dp[i][j+1] %= mod

ans = 0

for a in dp[-1]:
    ans += a
    ans %= mod

print(ans)


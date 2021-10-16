N,M = map(int, input().split())
mod = 10**9 + 7
dp = [0]*(N+1)
out = [False]*(N+1)
for _ in range(M):
    a = int(input())
    out[a] = True

dp[0] = 1
if not out[1]:
    dp[1] = 1
#* 貰うdp
for i in range(2,N+1):
    if out[i]:
        continue
    dp[i] += dp[i-1] + dp[i-2]
    dp[i] %= mod

print(dp[N])
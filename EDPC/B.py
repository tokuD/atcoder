N,K = map(int, input().split())
H = [0] + list(map(int,input().split()))
INF = 10 ** 10
dp = [INF]*(N+1)

dp[1] = 0

#* 配るdp
for i in range(1,N):
    for k in range(1,K+1):
        j = i + k
        if  j <= N:
            dp[j] = min(dp[j],dp[i] + abs(H[i]-H[j]))

print(dp[-1])
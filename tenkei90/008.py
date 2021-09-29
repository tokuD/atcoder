N = int(input())
S = list(input())
mod = 10**9+7

dp = [[0 for j in range(8)] for i in range(N+1)]
dp[0][0] = 1
converter = {'a':1,'t':2,'c':3,'o':4,'d':5,'e':6,'r':7}
for i in range(N):
    for j in range(8):
        dp[i+1][j] += dp[i][j]
        try:
            if j + 1 == converter[S[i]]:
                dp[i+1][j+1] += dp[i][j]
        except KeyError:
            continue
print(dp[-1][-1]%mod)

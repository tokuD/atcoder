N = int(input())
X,Y = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
INF = 10 ** 5
dp = [[INF]*(Y+1) for _ in range(X+1)]
dp[0][0] = 0

for n in range(N):
    a,b = AB[n]
    for i in range(X+1)[::-1]:
        for j in range(Y+1)[::-1]:
            if dp[i][j] == INF:
                continue
            if i + a <= X and j + b <= Y:
                dp[i+a][j+b] = min(dp[i+a][j+b],dp[i][j]+1)
            elif i + a <= X and j + b > Y:
                dp[i+a][-1] = min(dp[i+a][-1],dp[i][j]+1)
            elif i + a > X and j + b <= Y:
                dp[-1][j+b] = min(dp[-1][j+b],dp[i][j]+1)
            elif i + a > X and j + b > Y:
                dp[-1][-1] = min(dp[-1][-1],dp[i][j]+1)



if dp[-1][-1] == INF:
    print(-1)
else:
    print(dp[-1][-1])
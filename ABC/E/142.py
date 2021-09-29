N,M = map(int, input().split())
A = [0]
C = [[0]]
for i in range(M):
    a,b = map(int, input().split())
    c = list(map(int, input().split()))
    A.append(a)
    C.append(c)
INF = 10**10
#* dp[i][j] = n : i個目までの鍵でj(2進数で宝箱と対応)の宝箱を開けるのに必要な最小費用
dp = [[INF]*(2**N) for _ in range(M+1)]
dp[0][0] = 0

O = [0]
#* i個目の鍵で開けられる宝箱を先に計算
for i in range(1,M+1):
    o = 0
    for j in range(1,N+1):
        if j in C[i]:
            o += 2**(j-1)
    O.append(o)

#* 配るdp
for i in range(M):
    for j in range(2**N):

        #* あり得ない場合はスキップ
        if dp[i][j] == INF:
            continue

        #* (i+1)個目の鍵を買わない場合
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])

        #* (i+1)個目の鍵を買う場合
        dp[i+1][j|O[i+1]] = min(dp[i+1][j|O[i+1]],dp[i][j]+A[i+1])

ans = INF
for i in range(M+1):
    ans = min(ans,dp[i][-1])

if ans == INF:
    print(-1)
else:
    print(ans)
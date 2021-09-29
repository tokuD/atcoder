N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
INF = 10**12
#* dp[i][j][c,k] : i個の都市を回って行った都市はj、コストはc、直前に寄った都市はk
dp = [[[INF for i in range(2)] for j in range(2**N)]for _ in range(N+1)]
dp[0][0][0] = 0
dp[0][0][1] = 0

#* 配るdp
for i in range(N):
    for j in range(2**N):

        #* あり得ない場合スキップ
        if dp[i][j][0] == INF:
            continue

        #* 直前に行った都市
        pre = dp[i][j][1]

        #* まだ行っていない都市へ行った時に最小コストなら更新
        for k in range(1,N):
            #* 既に行ってる場合
            if j >> k & 1:
                continue
            #* まだ行ってない場合
            else:
                if dp[i][j][0] + A[pre][k] < dp[i+1][j|(2**k)][0]:
                    dp[i+1][j|(2**k)][0] = dp[i][j][0] + A[pre][k]
                    dp[i+1][j|(2**k)][1] = k

        #* 0に戻るとき
        if i == N-1 and (j|1) == 2**N-1:
            if dp[i][j][0] + A[pre][0] < dp[i+1][j|1][0]:
                dp[i+1][j|1][0] = dp[i][j][0] + A[pre][0]
                dp[i+1][j|1][1] = 0

print(dp[-1][-1][0])
# print(dp)

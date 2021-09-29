N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
INF = 10**12
#* dp[i][j]:回った都市がi,直前の都市がjの時の最小コスト
dp = [[INF]*N for _ in range(2**N)]
dp[0][0] = 0

for i in range(2**N-1):
    for pre in range(N):
        #* あり得ない場合スキップ
        if dp[i][pre] == INF:
            continue

        #* まだ通っていない都市に行く
        for nex in range(N):
            if (i >> nex) & 1:
                continue
            if nex == 0:
                if (i|(2**nex)) == 2**N-1:
                    dp[-1][nex] = min(dp[-1][nex],dp[i][pre]+A[pre][nex])
            else:
                dp[i|(2**nex)][nex] = min(dp[i|(2**nex)][nex],dp[i][pre]+A[pre][nex])
print(min(dp[-1]))


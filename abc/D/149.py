N,K = map(int, input().split())
R,S,P = map(int, input().split())
T = list(input())
#* enemy[i][j]: N%k=iのグループでj番目の手
enemy = [[] for _ in range(K)]
for i in range(N):
    enemy[i%K].append(T[i])

#* dp[i][j][k]:Kの余りがiのグループのj番目に出す手がkの場合の最大ポイント
dp = [[[0 for k in range(3)] for j in range(N//K+1)] for i in range(K)]


for i in range(K):
    for k in range(3):
        if enemy[i][0] == 's':
            dp[i][0][0] = R
        if enemy[i][0] == 'p':
            dp[i][0][1] = S
        if enemy[i][0] == 'r':
            dp[i][0][2] = P
count = 1
#* 配るdp
for i in range(K):
    for j in range(N//K):
        for k in range(3):

            try:
                #* グーを出す場合
                if k!=0:
                    if enemy[i][j+1] == 's':
                        dp[i][j+1][0] = max(dp[i][j+1][0],dp[i][j][k]+R)
                    else:
                        dp[i][j+1][0] = max(dp[i][j+1][0],dp[i][j][k])

                #* チョキを出す場合
                if k!=1:
                    if enemy[i][j+1] == 'p':
                        dp[i][j+1][1] = max(dp[i][j+1][1],dp[i][j][k]+S)
                    else:
                        dp[i][j+1][1] = max(dp[i][j+1][1],dp[i][j][k])

                #* パーを出す場合
                if k!=2:
                    if enemy[i][j+1] == 'r':
                        dp[i][j+1][2] = max(dp[i][j+1][2],dp[i][j][k]+P)
                    else:
                        dp[i][j+1][2] = max(dp[i][j+1][2],dp[i][j][k])
            except IndexError:
                break

ans = 0
for i in range(K):
    a = max(dp[i][-1])
    if a == 0:
        a = max(dp[i][-2])
    ans += a

print(ans)


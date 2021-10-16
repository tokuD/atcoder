N,M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]

INF = 10**9
ans = [0] * N
for i in range(N):
    min_dis = INF
    for j in range(M):
        now_dis = abs(AB[i][0]-CD[j][0]) + abs(AB[i][1]-CD[j][1])
        if now_dis < min_dis:
            ans[i] = j
            min_dis = now_dis

for a in ans:
    print(a+1)
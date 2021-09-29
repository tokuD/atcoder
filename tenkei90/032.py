from itertools import permutations

N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
M = int(input())
enemy = [list(map(int,input().split())) for i in range(M)]
out = [[False for j in range(N)] for i in range(N)]
for i in range(M):
    out[enemy[i][0]-1][enemy[i][1]-1] = True
    out[enemy[i][1]-1][enemy[i][0]-1] = True
member = [i for i in range(N)]
ans = -10**4
# print(out)
for order in permutations(member):
    total = 0
    flag = True
    for j in range(N-1):
        if out[order[j]][order[j+1]]:
            flag = False
    if flag:
        for j in range(N):
            total += A[order[j]][j]
        ans = min(abs(ans),total)
        # print(order, total)

print(max(ans,-1))

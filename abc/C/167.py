N,M,X = map(int,input().split())
A = []
C = []
cost = []

for i in range(N):
    row = list(map(int,input().split()))
    C.append(row[0])
    A.append(row[1:])

for i in range(2**N):
    total = [0] * M
    c = 0
    flag = True
    for j in range(N):
        if i & (1<<j):
            c += C[j]
            for k in range(M):
                total[k] += A[j][k]
    for k in range(M):
        if total[k] < X:
            flag = False
    if flag:
        cost.append(c)

try:
    print(min(cost))
except ValueError:
    print(-1)

N,M,C = map(int, input().split())
B = list(map(int, input().split())) #! M個の整数
ans = 0

A = [] #! d1:N個のソースコード、d2:M個の特徴
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)

for i in range(N):
    total = 0
    for j in range(M):
        total += A[i][j] * B[j]
    if total + C > 0:
        ans += 1

print(ans)

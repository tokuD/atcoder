K,N = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
kyori = 0

for i in range(N):
    a = 0
    if i == N-1:
        a = A[0] - A[i]
    else:
        a = A[i+1] - A[i]
    if a < 0:
        a += K
    if a > kyori:
        kyori = a

print(K-kyori)

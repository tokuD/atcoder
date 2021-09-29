N = int(input())
A = list(map(int, input().split()))
X = int(input())
total = sum(A)

loop = X // total
X = X % total

add = 0

for i in range(N):
    add += A[i]
    if X < add:
        ans = loop * N + i + 1
        print(ans)
        exit()

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
a = - (N-1)
for i in range(N):
    ans += a * A[i]
    a += 2

print(ans)
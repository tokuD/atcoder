N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
S1 = 0
S2 = 0

for a in A:
    S1 += a
    S2 += a**2

ans = (S1**2 - S2) // 2
ans %= mod
print(ans)

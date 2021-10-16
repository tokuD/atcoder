from typing import List
N = int(input())
A = list(map(int, input().split()))
S1 = 0
S2 = 0
for a in A:
    S1 += a
    S2 += a**2

ans = 0

for a in A:
    ans += N*(a**2) - 2*a*S1 + S2

print(ans//2)
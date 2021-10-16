from collections import defaultdict
import math
N = int(input())

def f(n):
    return n*(n+1)//2

#* Nを素因数分解
#* prime[i]:素数iで何回割れるか
prime = defaultdict(int)
skip = [False]*(int(math.sqrt(N))+1)

for i in range(2,int(math.sqrt(N))+1):
    if skip[i]:
        continue
    count = i
    while N % i == 0:
        N //= i
        prime[i] += 1
        if count <= int(math.sqrt(N)):
            skip[count] = True
            count *= i
if N != 1:
    prime[N] += 1

def binary_search(x):
    ok = 1
    ng = x
    while ng - ok > 1:
        mid = (ok+x)//2
        if f(mid) <= x:
            ok = mid
        else:
            ng = mid
    return ok

ans = 0
for p,x in prime.items():
    ans += binary_search(x)
print(ans)
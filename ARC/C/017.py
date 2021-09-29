from bisect import bisect_left
N,X = map(int,input().split())
W = [int(input()) for _ in range(N)]
W1 = W[:N//2]
W2 = W[N//2:]
n = N//2
m = N - (N//2)
g1 = {}
g2 = {}
for i in range(2**n):
    total = 0
    for j in range(n):
        if (i >> j) & 1:
            total += W[j]
    try:
        g1[total] += 1
    except KeyError:
        g1[total] = 1

for i in range(2**m):
    total = 0
    for j in range(m):
        if (i >> j) & 1:
            total += W[n+j]
    try:
        g2[total] += 1
    except KeyError:
        g2[total] = 1

ans = 0
for w1,count1 in g1.items():
    w2 = X - w1
    count2 = 0
    try:
        count2 = g2[w2]
    except KeyError:
        pass
    ans += count1 * count2

print(ans)
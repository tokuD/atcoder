N = int(input())
A = []
P = []
X = []
for _ in range(N):
    a,p,x = map(int, input().split())
    A.append(a)
    P.append(p)
    X.append(x)
INF = 10**10
ans = INF

for i in range(N):
    a = A[i]
    p = P[i]
    x = X[i]
    x -= a
    if x > 0:
        ans = min(ans,p)

print(ans if ans != INF else -1)
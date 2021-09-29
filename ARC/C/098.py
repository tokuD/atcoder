N = int(input())
S = list(input())
W = [0]*N
E = [0]*N
if S[0] == 'W':
    W[0] = 1
else:
    E[0] = 1

for i in range(1,N):
    W[i] = W[i-1]
    E[i] = E[i-1]
    s = S[i]
    if s == 'W':
        W[i] += 1
    else:
        E[i] += 1

ans = N
for i in range(N):
    l = W[i-1]
    r = E[N-1] - E[i]
    if i == 0:
        l = 0
    if i == N-1:
        r = 0
    ans = min(ans,l+r)

print(ans)
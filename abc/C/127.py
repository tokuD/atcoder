N,M = map(int, input().split())
q = []

for i in range(M):
    l,r = map(lambda x:int(x)-1, input().split())
    q.append([l,1])
    q.append([r+1,-1])

q.sort(key=lambda x:x[0])

imos = [0]*(N+1)

for i in range(2*M):
    a,b = q[i]
    imos[a] += b
count = 0
ans = [0]*N
ans[0] = imos[0]
if ans[0] == M:
    count += 1
for i in range(1,N):
    ans[i] += ans[i-1] + imos[i]
    if ans[i] == M:
        count += 1

print(count)



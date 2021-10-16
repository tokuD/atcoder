a,b = map(int, input().split())
c,d = map(int, input().split())
INF = 10**10
ans = -INF
for x in range(a,b+1):
    for y in range(c,d+1):
        ans = max(ans,x-y)

print(ans)
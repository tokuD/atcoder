N,X = map(int, input().split())
ans = -1
total = 0

for i in range(1,N+1):
    v,p = map(int, input().split())
    total += v * p
    print(total)
    if total > X * 100:
        ans = i
        break
print(ans)
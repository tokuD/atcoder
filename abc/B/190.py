N,S,D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
ans = 'No'

for i in range(N):
    x,y = XY[i]
    if x < S and y > D:
        ans = 'Yes'

print(ans)
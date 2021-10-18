N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    x1,y1 = XY[i]
    for j in range(i+1,N):
        x2,y2 = XY[j]
        a = (y2-y1) / (x2-x1)
        if -1 <= a <= 1:
            ans += 1

print(ans)
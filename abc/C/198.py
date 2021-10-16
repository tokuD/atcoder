import math
R,X,Y = map(int, input().split())
dis = math.sqrt(X**2+Y**2)
ans = int(dis//R)
if dis % R != 0:
    ans += 1
    if ans == 1:
        ans += 1

print(ans)
x,y = map(int, input().split())
ans = 0

if abs(x) == abs(y):
    ans = 1
elif x > 0 and y > 0:
    if x<y:
        ans = y - x
    else:
        ans = x - y + 2
elif x > 0 and y < 0:
    ans = abs(abs(x)-abs(y)) + 1
elif x < 0 and y > 0:
    if abs(x) < abs(y):
        ans = abs(y) - abs(x) + 1
    else:
        ans = abs(x) - abs(y) + 1
elif x < 0 and y < 0:
    if abs(x) < abs(y):
        ans = abs(y) - abs(x) + 2
    else:
        ans = abs(x) - abs(y)
elif x == 0 and y != 0:
    if y > 0:
        ans = y
    else:
        ans = abs(y) + 1
elif x != 0 and y == 0:
    if x > 0:
        ans = x + 1
    else:
        ans = abs(x)


print(ans)
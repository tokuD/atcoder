from re import X


x,y = map(int, input().split())

ans = x

if x == y:
    ans = x
else:
    for i in range(3):
        if i in [x,y]:
            continue
        else:
            ans = i

print(ans)

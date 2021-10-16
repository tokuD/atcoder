R,B = map(int, input().split())
x,y = map(int, input().split())

ok = 0
ng = 10**18+1

while ng - ok > 1:
    mid = (ok+ng)//2 #* midは2種類の花束の合計
    r = 0
    l = mid + 1

    #* 合計がmidの時に条件を満たせるか
    while l - r > 1:
        a = (r+l)//2
        b = mid - a
        if (a*x+b<=R) and (a+b*y<=B):
            ok = mid
            break
        elif (a*x+b<=R) and (a+b*y>B):
            r = a
        elif (a*x+b>R) and (a+b*y<=B):
            l = a
        else:
            ng = mid
            break
    a = (r+l)//2
    b = mid - a
    if (a*x+b<=R) and (a+b*y<=B):
        ok = mid
    else:
        ng = mid

print(ok)
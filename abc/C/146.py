from math import log10
A,B,X = map(int, input().split())
ok = 0
ng = 10**9+1

while ng - ok > 1:
    mid = (ok+ng)//2
    if A*mid + B*(int(log10(mid))+1) <= X:
        ok = mid
    else:
        ng = mid
print(ok)
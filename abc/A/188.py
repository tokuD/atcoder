X,Y = map(int, input().split())

mi = min(X,Y)
ma = max(X,Y)
if mi + 3 > ma:
    print('Yes')
else:
    print('No')
N = int(input())
A = list(map(int,input().split()))
A = A[:N]
n = len(A)
kaburi = {}
for i in range(n):
    try:
        kaburi[A[i]] += 1
    except KeyError:
        kaburi[A[i]] = 0

ans = 0
for key,value in kaburi.items():
    if value == 0:
        ans += n-1
    else:
        ans += (value+1)*(n-value-1)


print(int(ans/2))

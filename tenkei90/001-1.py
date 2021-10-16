N,L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def count(x):
    """
    x以上になったら切れ目を入れる
    切れ目の数を返す
    """
    piece = 0
    res = 0
    last = 0
    for i in range(N):
        if x <= (A[i]-last) and x <= (L - A[i]):
            res += 1
            last = A[i]
    return res

ok = -1
ng = sum(A)

while ng-ok>1:
    mid = (ok+ng)//2
    pieces = count(mid)
    if K <= pieces:
        ok = mid
    else:
        ng = mid

print(ok)
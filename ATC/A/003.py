from bisect import bisect_left
N,K = map(int,input().split())
A = list(map(int, input().split()))

# ng = -1
# ok = N

# while (ok - ng) > 1:
#     mid = (ok+ng)//2
#     if K <= A[mid]:
#         ok = mid
#     else:
#         ng = mid

# if ok == N:
#     print(-1)
# else:
#     print(ok)

ans = bisect_left(A, K)
if ans == N:
    print(-1)
else:
    print(ans)
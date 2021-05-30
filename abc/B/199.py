N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()
ans = 0
if B[0] - A[0] >= 0:
    ans = B[0] - A[0] + 1


print(ans)

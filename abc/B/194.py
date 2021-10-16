N = int(input())
A = []
B = []

for i in range(N):
    a,b = map(int, input().split())
    A.append([a,i])
    B.append([b,i])

A.sort()
B.sort()

ans = 0

if A[0][1] != B[0][1]:
    ans = max(A[0][0], B[0][0])
else:
    ans = min(A[0][0]+B[0][0], max(A[0][0],B[1][0]),max(A[1][0],B[0][0]))

print(ans)
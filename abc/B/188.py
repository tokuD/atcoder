N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for i in range(N):
    a = A[i]
    b = B[i]
    ans += a*b

if ans == 0:
    print('Yes')
else:
    print('No')
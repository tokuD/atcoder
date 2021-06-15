import enum


N = int(input())
A = list(map(int, input().split()))
ans = [0 for i in range(N)]
for i,a in enumerate(A):
    ans[a-1] = str(i+1)

# print(ans)
print(' '.join(ans))

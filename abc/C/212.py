N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = []
for i in range(N):
    C.append((A[i],0))
for i in range(M):
    C.append((B[i],1))

C.sort()
ans = 10**9
flag = 0
for i in range(N+M-1):
    if C[i][1] != C[i+1][1]:
        ans = min(ans,C[i+1][0]-C[i][0])
print(ans)

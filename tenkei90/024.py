N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dif = 0
ans = 'Yes'
for i in range(N):
    dif += abs(A[i]-B[i])

if dif > K:
    ans = 'No'
elif (K-dif) % 2 != 0:
    ans = 'No'

print(ans)

N,X = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
    if (i+1) % 2 == 0:
        X -= A[i]-1
    else:
        X -= A[i]
    if X < 0:
        print('No')
        exit()
print('Yes')

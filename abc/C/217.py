N = int(input())
p = list(map(int,input().split()))
q = [0] * N
for i in range(N):
    q[p[i]-1] = i+1

for i in range(N-1):
    print(q[i],end=' ')
print(q[-1])

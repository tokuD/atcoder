A,B,N = map(int,input().split())
ans = []
for i in range(1,N+1):
    ans.append([i,int(A*i/B)-A*int(i/B)])

print(ans)

for i in range(1,min(N+1,B+1)):

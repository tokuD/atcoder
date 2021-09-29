N = int(input())
A = list(map(int,input().split()))
a = []
for i in range(N):
    a.append([A[i],i+1])

a.sort(reverse=True)
print(a[1][1])

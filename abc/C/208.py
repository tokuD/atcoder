N,K = map(int, input().split())
A = list(map(int, input().split()))

#* [国民番号,i人目,お菓子の数]
ans = []

for i in range(N):
    a = A[i]
    ans.append([a,i,K//N])

ans.sort(key=lambda x:x[0])

rest = K % N

for i in range(rest):
    ans[i][2] += 1

ans.sort(key=lambda x:x[1])

for a in ans:
    print(a[2])

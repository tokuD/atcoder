from sys import stdin
H,W = list(map(int,stdin.readline().rstrip().split()))
A = [list(map(int,stdin.readline().rstrip().split())) for i in range(H)]
row = [] #!各行の合計
column = [0]*W #!各列の合計

for a in A:
    row.append(sum(a))
    for i in range(W):
        column[i] += a[i]

for i in range(H):
    ans = []
    for j in range(W):
        ans.append(row[i]+column[j]-A[i][j])
    print(*ans)

N = int(input())
A = list(map(int, input().split()))

#* [-1, 0, 1, ..., max(A)+1]
ans = [0]*(max(A)+3)

for a in A:
    ans[a] += 1
    ans[a+1] += 1
    ans[a+2] += 1

print(max(ans))
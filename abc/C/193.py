import math
N = int(input())
n = int(math.sqrt(N))
#* 表せたらsetに入れる
ans = set()

for i in range(2,n+1):
    j = 2
    while i**j <= N:
        ans.add(i**j)
        j += 1

print(N-len(ans))
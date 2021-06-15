N,M,X = map(int, input().split())
A = list(map(int, input().split()))
a1 = 0
a2 = 0

for a in A:
    if a < X:
        a1 += 1
    if a > X:
        a2 += 1


print(min(a1,a2))

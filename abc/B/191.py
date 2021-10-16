N,X = map(int, input().split())
A = list(map(int, input().split()))
ans = []

for a in A:
    if a != X:
        ans.append(str(a))

if len(ans) == 0:
    print()
else:
    print(' '.join(ans))
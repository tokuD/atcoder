from itertools import permutations
N = list(input())
cut = []
ans = 0
count = 0
for n in permutations(N):
    for i in range(1,len(n)):
        a = n[:i]
        b = n[i:]
        if a[0] == '0' or b[0] == '0':
            continue
        x = int(''.join(a))
        y = int(''.join(b))
        ans = max(ans,x*y)

print(ans)
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1,N):
        t0,l0,r0 = L[i]
        t1,l1,r1 = L[j]

        if (r0<l1) or (r1<l0):
            continue

        if r0 == l1:
            if t0 == 2 or t0 == 4:
                continue
            if t1 == 3 or t1 == 4:
                continue

        if r1 == l0:
            if t0 == 3 or t0 == 4:
                continue
            if t1 == 2 or t1 == 4:
                continue

        ans += 1

print(ans)
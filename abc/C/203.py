N, K = map(int, input().split())
tomo = []
for _ in range(N):
    a, b = map(int, input().split())
    tomo.append([a, b])

tomo = sorted(tomo, key=lambda x:x[0])
ans = 0

if K < tomo[0][0]:
    pass
else:
    for mura, kane in tomo:
        if K >= mura:
            K += kane


if K >= 10**100:
    K = 10**100

print(K)

N = int(input())
A = list(map(int, input().split()))

ans = 0

for a in A:
    if a <= 10:
        continue
    else:
        ans += a - 10

print(ans)

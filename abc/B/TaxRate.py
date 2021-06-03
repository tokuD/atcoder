N = int(input())
ans = ':('
for x in range(1, 50000):
    if N == int(x*1.08):
        ans = x
        break

print(ans)

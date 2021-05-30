N = int(input())
t = [0]
x = [0]
y = [0]

for _ in range(N):
    a, b, c = map(int, input().split())
    t.append(a)
    x.append(b)
    y.append(c)

ans = "Yes"

for i in range(N):
    n = t[i+1] - t[i]
    l = abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])
    if (l <= n) and ((n-l) % 2 == 0):
        pass
    else:
        ans = "No"
        break

print(ans)

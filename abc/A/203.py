a, b, c = map(int, input().split())
ans = 0
if a == b:
    ans = c
elif b == c:
    ans = a
elif c == a:
    ans = b
print(ans)

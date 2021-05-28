a, b = map(int, input().split())
ans = ""

if a*b % 2 == 0:
    ans = "Even"
else:
    ans = "Odd"

print(ans)

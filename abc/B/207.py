A,B,C,D = map(int, input().split())
ans = 0
if C * D - B <= 0:
    ans = -1
else:
    ans = A // (C*D-B)
    if A % (C*D-B) != 0:
        ans += 1

print(ans)
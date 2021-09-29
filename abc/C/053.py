x = int(input())
syou = x // 11
amari = x % 11
ans = syou * 2
if amari == 0:
    pass
elif amari <= 6:
    ans += 1
else:
    ans += 2

print(ans)

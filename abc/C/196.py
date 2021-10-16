N = int(input())
ans = 0

for i in range(1,10**7):
    x = list(str(i)) + list(str(i))
    if N < int(''.join(x)):
        break
    ans += 1

print(ans)
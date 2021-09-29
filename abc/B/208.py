P = int(input())
coin = []
k = 1
ans = 0
for i in range(1,11):
    k *= i
    coin.append(k)

for i in range(0,10)[::-1]:
    quo = P // coin[i]
    if quo > 0:
        P %= coin[i]
        ans += quo

print(ans)

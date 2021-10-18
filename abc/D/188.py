from collections import defaultdict
N,C = map(int, input().split())
dic = defaultdict(int)
for _ in range(N):
    a,b,c = map(int, input().split())
    dic[a] += c
    dic[b+1] -= c
outcome = sorted(dic.items())
now = 0
ans = 0
for i in range(len(outcome)-1):
    day1, price = outcome[i]
    day2 = outcome[i+1][0]
    now += price
    ans += min(now,C) * (day2-day1)

print(ans)
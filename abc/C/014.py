from collections import defaultdict
N = int(input())
color = []
for i in range(N):
    a,b = map(int, input().split())
    color.append([a,0])
    color.append([b+1,1])

color.sort(key=lambda x:(x[0],x[1]))
dic = defaultdict(int)
for i,j in color:
    if j == 0:
        dic[i] += 1
    if j == 1:
        dic[i] -= 1
dic_sorted = sorted(dic.items(),key=lambda x:x[0])
ans = 0
now = 0

for key,value in dic_sorted:
    now += value
    ans = max(ans,now)

print(ans)
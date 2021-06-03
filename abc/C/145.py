from itertools import permutations

N = int(input())
xy = [] #? [(x1,y1), (x2,y2), ...] d1:家番号、d2:座標
house = [i for i in range(N)]
for _ in range(N):
    x, y = map(int, input().split())
    xy.append((x,y))

#! 先に家と家の距離を全パターン計算
dis = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            a = xy[i]
            b = xy[j]
            dis[i][j] = (  (a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
# print(dis)
total = 0
count = 0
for keiro in permutations(house):
    for i in range(N-1):
        total += dis[keiro[i]][keiro[i+1]]
    count += 1

print(total/count)

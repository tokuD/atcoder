from collections import defaultdict
from itertools import combinations
N = int(input())
X = defaultdict(list)
Y = defaultdict(list)
point = []
for i in range(N):
    x,y = map(int,input().split())
    Y[x].append(y)
    X[y].append(x)
    point.append([x,y])

ans = 0

for i,j in combinations(range(N), 2):
    x0,y0 = point[i]
    x1,y1 = point[j]
    if x0 == x1 or y0 == y1:
        continue
    if x0 in X[y1] and x1 in X[y0]:
        ans += 1



print(ans//2)
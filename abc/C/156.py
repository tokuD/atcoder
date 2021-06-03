from itertools import permutations
N = int(input())
X = list(map(int, input().split()))
totals =[]

for p in range(1, 101):
    total = 0
    for x in X:
        total += (x-p)**2
    totals.append(total)

totals.sort()

print(totals[0])

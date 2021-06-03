from itertools import permutations

N, M = map(int, input().split()) #? N:頂点、M:辺
ab1 = [] #? [(a1,b1), (a2,b2), ...]
ab2 = []

for _ in range(M):
    a,b = map(int, input().split())
    ab1.append((a,b))
    ab2.append((b,a))

lines = [i for i in range(2,N+1)]

total = 0

for line in permutations(lines):
    flag = True
    line = list(line)
    line.insert(0,1)
    for i in range(N-1):
        load = (line[i], line[i+1])
        if load in ab1 or load in ab2:
            continue
        else:
            flag = False
            break
    if flag:
        # print(line)
        total += 1

print(total)

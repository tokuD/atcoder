from itertools import permutations
N,M = map(int, input().split())
AB = [tuple(map(int,input().split())) for i in range(M)]
keiros = [[i+1]for i in range(N)] #? d1:都市i d2:その都市から行ける都市
ans = 0

for ab in AB:
    keiros[ab[0]-1].append(ab[1])

for k in range(len(keiros)):
    for i in range(len(keiros[k])):
        for j in range(len(keiros[keiros[k][i]-1])):
            if not keiros[keiros[k][i]-1][j] in keiros[k]:
                keiros[k].append(keiros[keiros[k][i]-1][j])

for k in range(len(keiros)):
    for i in range(len(keiros[k])):
        for j in range(len(keiros[keiros[k][i]-1])):
            if not keiros[keiros[k][i]-1][j] in keiros[k]:
                keiros[k].append(keiros[keiros[k][i]-1][j])

for keiro in keiros:
    ans += len(keiro)

print(ans)

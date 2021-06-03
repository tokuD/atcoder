from itertools import permutations
N,A,B = map(int, input().split())
S = list(input())

ans = []
total = 0
foreigner = 0

for s in S:
    if (s == 'a') and (total < (A+B)):
        total += 1
        ans.append('Yes')
    elif (s == 'b') and (total < (A+B)) and (foreigner+1 <= B):
        total += 1
        foreigner += 1
        ans.append('Yes')
    else:
        ans.append('No')

for a in ans:
    print(a)

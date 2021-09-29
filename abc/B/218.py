import string
P = list(map(int,input().split(' ')))
abc = list(string.ascii_lowercase)
ans = []
for i in range(len(P)):
    ind = P[i]
    ans.append(abc[ind-1])

print(''.join(ans))

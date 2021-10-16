X = list(input())
X.append('.')
ans = []
i = 0
while X[i] != '.':
    ans.append(X[i])
    i += 1

print(''.join(ans))

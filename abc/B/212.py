X = list(input())
X = list(map(int,X))
# print(X)
ans = 'Strong'
if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
    ans = 'Weak'

flag = True
for i in range(3):
    if X[i] == 9:
        if X[i+1] != 0:
            flag = False
    else:
        if X[i+1] != X[i] + 1:
            flag = False
if flag:
    ans = 'Weak'

print(ans)

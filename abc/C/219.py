X = list(input())
N = int(input())
S = [list(input()) for _ in range(N)]
dict_ = {}
for i in range(len(X)):
    dict_[X[i]] = i
ans = [] # 名前、数字

for i in range(N):
    num = []
    for j in range(len(S[i])):
        num.append(dict_[S[i][j]])
    ans.append([num,S[i]])

ans.sort(key=lambda x:x[0])
for i in range(N):
    print(''.join(ans[i][1]))

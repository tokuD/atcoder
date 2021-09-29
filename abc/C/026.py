import sys
sys.setrecursionlimit(10**9)
N = int(input())
sub = [[] for _ in range(N)] #* sub[i]:社員iの直属の部下
salary = [0] * N #* salary[i]:社員iの給料

for i in range(1,N):
    b = int(input())
    sub[b-1].append(i)

def calc(i):
    """社員iの給料を返す"""

    #* 既に計算していれば持ってくる
    if salary[i] != 0:
        return salary[i]

    #* 直属の部下がいなければ1
    if len(sub[i]) == 0:
        salary[i] = 1
        return 1

    #* 直属の部下がいる時
    ma = 0
    mi = 10**6
    for j in range(len(sub[i])):
        a = calc(sub[i][j])
        ma = max(ma,a)
        mi = min(mi,a)
    salary[i] = ma + mi + 1
    return salary[i]

print(calc(0))

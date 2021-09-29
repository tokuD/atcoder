from collections import deque

N = int(input())
ans = 0
Q = deque()
Q.append(0)

#* 幅優先探索
while len(Q) > 0:

    #* 3,5,7のflag
    flag = True

    #* queから取り出し
    x = Q.popleft()

    #* Nを越えたらスキップ
    if N < x:
        continue

    #* 3,5,7があればans += 1
    for i in ['3','5','7']:
        if not i in list(str(x)):
            flag = False
    if flag:
        ans += 1

    #* 3,5,7を追加
    for i in [3,5,7]:
        Q.append(10*x+i)

print(ans)
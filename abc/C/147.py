N = int(input())
syougen = []#? [[[x1,y1], [x2,y2],], [[x1,y1], [x2,y2]], ] d1:人、d2:証言、d3:xとy
A = [] #? [A1, A2, ...] i人目の証言数
ans = 0
for _ in range(N):
    i = int(input())
    A.append(i)
    xy = [] #! [[x1,y1], [x2,y2], ]
    for _ in range(i):
        row = list(map(int, input().split())) #! [x, y]
        xy.append(row)
    syougen.append(xy)

#? 正直・不親切の人の全パターン探索
for i in range(2**N):#!2進数で桁が人を、0 or 1が正直・不親切を表す
    flag = True
    total = 0
    for n in range(N):#! n人目が正直か
        if (i>>n)&1 == 1 and flag:
            # total += 1
            for a in range(A[n]):
                syoujiki = syougen[n][a]
                if syoujiki[1] == 1 and (i>>(syoujiki[0]-1))&1 == 0:
                    flag = False
                    break
                if syoujiki[1] == 0 and (i>>(syoujiki[0]-1))&1 == 1:
                    flag = False
                    break
            total += 1
    if flag and total >= ans:
        ans = total

print(ans)

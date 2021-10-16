S = list(input())
T = list(input())
if S == T:
    print('Yes')
    exit()

count = []
for i in range(len(T)):
    s = S[i]
    t = T[i]
    if s != t:
        count.append([i,s,t])


if len(count) != 2:
    print('No')
    exit()

if len(count) == 2:
    if count[1][0] - count[0][0] == 1:
        s0,t0 = count[0][1:]
        s1,t1 = count[1][1:]
        if s0 == t1 and s1 == t0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')


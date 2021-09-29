N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]
s = []
t = []
s1 = []
t1 = []

flag1 = False
flag2 = False

for i in range(N):
    if '#' in S[i]:
        flag1 = True
    if flag1:
        s.append(S[i])
    if '#' in T[i]:
        flag2 = True
    if flag2:
        t.append(T[i])

for i in range(len(s))[::-1]:
    if not '#' in s[i]:
        s.pop()
    else:
        break

for i in range(len(t))[::-1]:
    if not '#' in t[i]:
        t.pop()
    else:
        break


flag1 = False

for i in range(N):
    a = []
    for j in range(len(s)):
        a.append(s[j][i])
        if s[j][i] == '#':
            flag1 = True
    if flag1:
        s1.append(a)

for i in range(len(s1))[::-1]:
    if not '#' in s1[i]:
        s1.pop()
    else:
        break


flag = False
for i in range(N):
    a = []
    for j in range(len(t)):
        a.append(t[j][i])
        if t[j][i] == '#':
            flag = True
    if flag:
        t1.append(a)

for i in range(len(t1))[::-1]:
    if not '#' in t1[i]:
        t1.pop()
    else:
        break


if s1 == t1:
    print('Yes')
    exit()

t11 = [[0]*(len(t1[0])) for _ in range(len(t1))]

for i in range(len(t1)):
    for j in range(len(t1[0])):
        t11[i][j] = t1[len(t1)-i-1][len(t1[0])-j-1]


if s1 == t11:
    print('Yes')
    exit()

tt = [[0] * (len(t1)) for _ in range(len(t1[0]))]

for i in range(len(t1[0])):
    for j in range(len(t1)):
        tt[i][j] = t1[j][len(t1[0])-i-1]


if s1 == tt:
    print('Yes')
    exit()

tt1 = [[0]*(len(tt[0])) for _ in range(len(tt))]

for i in range(len(tt)):
    for j in range(len(tt[0])):
        tt1[i][j] = tt[len(tt)-i-1][len(tt[0])-j-1]

if s1 == tt1:
    print('Yes')
    exit()

print('No')

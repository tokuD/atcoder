from collections import deque

N,M = map(int,input().split())
bottle = [0] * M
top = [[] for _ in range(N)] #* 一番上にある色がどの筒に入ってるか[色][筒1,筒2]
operate = deque()
for i in range(M):
    k = int(input())
    a = deque(map(lambda x:int(x)-1,input().split())) #! i番目の筒に入ってる色(上から順番)
    bottle[i] = a
    top[a[0]].append(i)
count = 0
for color in range(N):
    if len(top[color]) == 2:
        operate.append(color)

for i in range(N):
    color = 0
    try:
        color = operate.popleft()
    except IndexError:
        print('No')
        exit()
    m_i,m_j = top[color]
    top[color] = []
    bottle[m_i].popleft()
    bottle[m_j].popleft()
    if len(bottle[m_i]) > 0:
        new_color1 = bottle[m_i][0]
        top[new_color1].append(m_i)
        if len(top[new_color1]) == 2:
            operate.append(new_color1)
    if len(bottle[m_j]) > 0:
        new_color2 = bottle[m_j][0]
        top[new_color2].append(m_j)
        if len(top[new_color2]) == 2:
            operate.append(new_color2)

print('Yes')

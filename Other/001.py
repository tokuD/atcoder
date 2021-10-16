from collections import deque
S = list(input())
inverse = 1
T = deque()
for s in S:
    if s == 'R':
        inverse *= -1
    else:
        if inverse == 1:
            if len(T)>0:
                if s == T[-1]:
                    T.pop()
                else:
                    T.append(s)
            else:
                T.append(s)
        else:
            if len(T)>0:
                if s == T[0]:
                    T.popleft()
                else:
                    T.appendleft(s)
            else:
                T.appendleft(s)

ans = []
if inverse == 1:
    ans = list(T)
else:
    ans = list(T)[::-1]

print(''.join(ans))
from collections import deque
S = deque(input())
a = S.popleft()
S.append(a)
print(''.join(S))
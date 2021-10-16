from collections import deque
N = list(input())
zero = 0

for i in range(len(N))[::-1]:
    if N[i] == '0':
        zero += 1
    else:
        break

S = deque(N)

for i in range(zero):
    S.pop()

mid = len(S) // 2
l = mid
r = mid
if len(S) % 2 != 0:
    r += 1
A = list(S)
if A[:l] == A[r:][::-1]:
    print('Yes')
else:
    print('No')
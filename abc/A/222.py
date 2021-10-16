from collections import deque
N = list(input())

ans = ['0','0','0']
ans = deque(ans)
for i in N:
    ans.append(i)

while len(ans) > 4:
    ans.popleft()
print(''.join(ans))

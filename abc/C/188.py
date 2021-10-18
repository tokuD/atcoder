from collections import deque
N = int(input())
A = list(map(int, input().split()))
Q = deque()
for i in range(2**N):
    Q.append([A[i],i+1])

while len(Q) > 2:
    rate1,num1 = Q.popleft()
    rate2,num2 = Q.popleft()
    if rate1 < rate2:
        Q.append([rate2,num2])
    else:
        Q.append([rate1,num1])

rate1,num1 = Q.popleft()
rate2,num2 = Q.popleft()
if rate1 < rate2:
    print(num1)
else:
    print(num2)


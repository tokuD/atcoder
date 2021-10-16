import heapq
q = int(input())
Q = []
add = 0
ans = []
for i in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        x = que[1] - add
        heapq.heappush(Q, x)
    elif que[0] == 2:
        add += que[1]
    else:
        x = heapq.heappop(Q)
        x += add
        ans.append(x)

for a in ans:
    print(a)

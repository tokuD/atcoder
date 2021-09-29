# from collections import deque


# Q = int(input())
# A = deque()

# for i in range(Q):
#     query = list(map(int,input().split()))
#     if query[0] == 1:
#         A.append(query[1])
#     elif query[0] == 2:
#         print(A.popleft())
#     else:
#         A = deque(sorted(A))

N = list(input())
odd = 0
even = 0
for i in range(1,len(N)+1):
    if i % 2 == 0:
        odd += int(N[-i])
    else:
        even += int(N[-i])

print(odd,even)

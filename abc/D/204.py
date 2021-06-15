N = int(input())
T = list(map(int, input().split()))
T.sort(reverse=True)
# print(T)
ans = 0
A = T[0]
B = T[1]
for i in range(2,N):
    if A > B:
        B += T[i]
    else:
        A += T[i]

print(max(A,B))

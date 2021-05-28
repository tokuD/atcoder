N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
b_list = []

for c in C:
    b = B[c-1]
    b_list.append(b)

D = [0 for _ in range(N)]

for b in b_list:
    D[b-1] += 1

for a in A:
    ans += D[a - 1]

print(ans)



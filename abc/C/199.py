N = int(input())
S = list(input())
Q = int(input())
T = []
A = []
B = []

for _ in range(Q):
    t, a, b = map(int, input().split())
    T.append(t)
    A.append(a)
    B.append(b)

# print(list(S[:N]))
# print(T)
# print(A)
# print(B)

for i in range(Q):
    if (T[i] == 1):
        a = S[A[i]-1]
        b = S[B[i]-1]
        S[A[i]-1] = b
        S[B[i]-1] = a
    if T[i] == 2:
        a = S[:N]
        b = S[-N:]
        S[:N] = b
        S[-N:] = a
    # print(S)

print(''.join(S))

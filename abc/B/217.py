S = [input() for _ in range(3)]
A = ['ABC','ARC','AGC','AHC']
# print(S)
for i in range(4):
    if A[i] in S:
        continue
    else:
        print(A[i])

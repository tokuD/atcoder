N, K = map(int, input().split())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)
print(A[:2, :2])
B = [0]*(K**2)
# for i in range(N-K+1):
#     for j in range(N-K+1):
#         B = A[i:i+K, j:j+K]

print(B)

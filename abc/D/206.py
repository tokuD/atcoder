N = int(input())
A = list(map(int,input()))
kaeru = []
for i in range(N//2):
    if A[i] == A[-i-1]:
        continue
    else:
        

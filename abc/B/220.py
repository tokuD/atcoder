K = int(input())
A,B = input().split()
A = list(A)
B = list(B)
a = 0
b = 0

for i in range(len(A)):
    x = int(A[-i-1]) * (K ** i)
    a += x

for i in range(len(B)):
    x = int(B[-i-1]) * (K ** i)
    b += x
print(a*b)
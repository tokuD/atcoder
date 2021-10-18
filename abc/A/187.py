A,B = list(input().split())
A = list(A)
B = list(B)
a = 0
b = 0
for x in A:
    a += int(x)
for y in B:
    b += int(y)

print(max(a,b))

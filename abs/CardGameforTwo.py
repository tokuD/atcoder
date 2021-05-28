N = int(input())
a = list(map(int, input().split()))
a.sort()
A = 0
B = 0

while len(a) !=0:
    A += a.pop(-1)
    if len(a) != 0:
        B += a.pop(-1)

print(A - B)

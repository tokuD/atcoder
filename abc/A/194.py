A,B = map(int, input().split())
x = A + B

if x >= 15 and B >= 8:
    print(1)
elif x >= 10 and B >= 3:
    print(2)
elif x >= 3:
    print(3)
else:
    print(4)
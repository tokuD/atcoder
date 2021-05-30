N, Y = map(int, input().split())
x, y, z = [-1 for _ in range(3)]

flag = False
for a in range(N+1):
    for b in range(N+1):
        if a*9000 + b*4000 + 1000*N == Y and N-(a+b) >= 0:
            x, y, z = [a, b, N-(a+b)]
            flag = True
            break
    if flag:
        break
print(x, y, z)



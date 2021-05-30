N, K = map(int, input().split())
heya = []

for i in range(1, N+1): #!階
    for j in range(1, K+1): #!号室
        a = str(i) + "0" + str(j)
        heya.append(int(a))

print(sum(heya))

import math

x = int(input())

while True:
    flag = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            flag = False
            x += 1
            break
    if flag:
        print(x)
        exit()

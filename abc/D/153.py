H = int(input())
n = 1
while True:
    if (2**(n-1)<=H) and (H<2**n):
        print(2**n-1)
        break
    n += 1

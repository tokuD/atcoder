N,K = input().split()

def eight_to_ten(N):
    N = list(N)
    N = list(map(int,N))
    l = len(N)
    ten = 0
    for i in range(l):
        ten += N[i]*(8**(l-i-1))
    # print(ten)
    return ten

def ten_to_nine(ten):
    nine = []
    while True:
        syou = ten // 9
        amari = ten % 9
        if amari == 8:
            nine.append('5')
        else:
            nine.append(str(amari))
        ten = syou
        if ten == 0:
            break
    # print(nine[::-1])
    # print("".join(nine[::-1]))
    return "".join(nine[::-1])


for i in range(int(K)):
    N = ten_to_nine(eight_to_ten(N))
# ten_to_nine(eight_to_ten(N))


print(int(N))

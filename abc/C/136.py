N = int(input())
H = list(map(int,input().split()))
H[0] -= 1
for i in range(1,N):
    if H[i-1] - H[i] <= 0:
        if H[i-1] < H[i]:
            H[i] -= 1
    else:
        print('No')
        exit()
print('Yes')

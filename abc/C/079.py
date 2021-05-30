numbers = list(map(int, input()))
kigou = ['-', '+']

for i in range(2**3):
    total = numbers[0]
    # print(bin(i))
    for j in range(3):
        # print(bin(i>>j), (i>>j)&1)
        if ((i >> j) & 1):
            total += numbers[j+1]
        else:
            total -= numbers[j+1]
    # print(total)
    if total == 7:
        ans = str(numbers[0]) + kigou[i&1] + str(numbers[1]) + kigou[(i>>1)&1] + str(numbers[2]) + kigou[(i>>2)&1] + str(numbers[3]) + '=7'
        print(ans)
        break

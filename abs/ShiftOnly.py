N = int(input())
A = list(map(int, input().split()))
ans = 0
flag = True

while flag:
    for a in A:
        if a % 2 != 0:
            flag = False
            break
        else:
            continue
    if flag:
        A = list(map(lambda x: x/2, A))
        ans += 1

print(ans)

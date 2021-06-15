s = int(input())
a = [s]
flag = True
ans = 1
while flag:
    ans += 1
    if s % 2 == 0:
        s /= 2
    else:
        s = 3 * s + 1
    if s in a:
        print(ans)
        exit()
    a.append(s)

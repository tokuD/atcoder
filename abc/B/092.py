N = int(input()) #!人数
D,X = map(int,input().split()) #! D:日数 X:残ったチョコ
A = [int(input()) for i in range(N)] #! それぞれの人が食べた日
ans = X

for a in A:
    date = 1
    while True:
        if date <= D:
            ans += 1
            date += a
        else:
            break

print(ans)

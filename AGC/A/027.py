N,x = map(int,input().split()) #? N:子供 x:お菓子
a = list(map(int,input().split())) #? 子供iが喜ぶお菓子の数
a.sort()
ans = 0
for i,okasi in enumerate(a):
    # print(x)
    if i == N-1:
        if okasi == x:
            x -= okasi
            ans += 1
    else:
        if okasi <= x:
            x -= okasi
            ans += 1
        else:
            break
print(ans)

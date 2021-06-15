A,B,C = map(int,input().split())
initial = [A,B,C]
ans = 0
flag = True
while flag:
    a,b,c = [A,B,C]
    if (A%2==0) and (B%2==0) and (C%2==0):
        A = (b+c)/2
        B = (c+a)/2
        C = (a+b)/2
        ans += 1
        if (A in initial) and (B in initial) and (C in initial):
            ans = -1
            break
    else:
        break

print(ans)

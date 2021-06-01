N = int(input())
ans = len(str(N))
for i in range(1, int(N**0.5+2)):
    a = 0
    b = 0
    if N % i == 0:
        a = i
        b = N // i
        kari = max(len(str(a)), len(str(b)))
        if kari <= ans:
            ans = kari

print(ans)

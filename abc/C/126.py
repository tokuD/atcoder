N,K = map(int, input().split())
ans = 0
#* サイコロの目:i
for i in range(1,N+1):
    p = 1 / N
    score = i
    while score <= K - 1:
        score *= 2
        p /= 2
    ans += p

print(ans)
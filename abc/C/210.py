N,K = map(int,input().split())
C = list(input().split())
candies = {}
ans = 0

for i in range(N-K+1):
    if i == 0:
        for j in range(K):
            try:
                candies[C[i+j]] += 1
            except KeyError:
                candies[C[i+j]] = 1
            ans = len(candies)
            # print(candies)
    else:
        # print(candies)
        candies[C[i-1]] -= 1
        if candies[C[i-1]] == 0:
            del candies[C[i-1]]
        try:
            candies[C[i+K-1]] += 1
        except KeyError:
            candies[C[i+K-1]] = 1
        ans = max(ans,len(candies))

print(ans)

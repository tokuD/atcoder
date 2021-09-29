def main():
    N,L = map(int,input().split())
    dp = [1 for i in range(N+1)]
    for i in range(N+1):
        if i >= L:
            dp[i] = dp[i-1] + dp[i-L]
    ans = dp[N] % (10**9+7)
    print(ans)

if __name__ == '__main__':
    main()

def main():
    S = input().rstrip()
    T = 'chokudai'
    I,J = len(T),len(S)
    mod = 10**9+7
    dp = [[0 for j in range(J+1)] for i in range(I+1)]
    dp[0][0] = 1
    for i in range(I+1):
        for j in range(J+1):
            if j == 0:
                continue
            dp[i][j] += dp[i][j-1]
            if S[j-1] == T[i-1]:
                dp[i][j] += dp[i-1][j-1]
    # print(dp)
    print(dp[-1][-1] % mod)
    # for i in range(I+1):
    #     print(dp[i])


if __name__ == '__main__':
    main()

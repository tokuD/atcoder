def main():
    N,K = map(int,input().split())
    mod = 10**9 + 7
    ans = 1
    if N > 3:
        ans *= K*(K-1)
        ans *= pow(K-2, N-2, mod)
    else:
        for i in range(N):
            ans *= K-i
    ans %= mod

    print(ans)

if __name__ == '__main__':
    main()


def pow(x,n):
    #! xのn乗の計算
    ans = 1
    #!nが0になるまで計算を続ける
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

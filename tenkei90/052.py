def main():
    N = int(input())
    A = [list(map(int,input().split())) for i in range(N)]
    ans = 1
    for i in range(N):
        ans *= sum(A[i]) % (10**9+7)
    ans %= 10**9 + 7
    print(ans)


if __name__ == '__main__':
    main()

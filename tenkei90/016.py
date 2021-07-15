
def main():
    N = int(input())
    coin = list(map(int,input().split()))
    coin.sort(reverse=True)
    A = N//coin[0]
    ans = 10**4
    for i in range(A+1)[::-1]:
        cash1 = N - coin[0]*i
        B = cash1//coin[1]
        for j in range(B+1)[::-1]:
            cash2 = cash1 - coin[1]*j
            C = cash2//coin[2]
            if coin[0]*i + coin[1]*j + coin[2]*C == N:
                ans = min(ans,i+j+C)
    print(ans)



if __name__ == '__main__':
    main()

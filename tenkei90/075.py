import math

def prime(N,n=0):
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            n += 1
            # print(N//i)
            return prime(N//i,n)
    return n+1


def main():
    N = int(input())
    n = prime(N)
    ans = n // 2 + 1
    dp = [0 for i in range(n+1)]
    for i in range(1,n+1):
        if i == 1:
            dp[i] = 0
        elif i % 2 == 0:
            dp[i] = 1 + dp[i//2]
        else:
            dp[i] = 1 + dp[(i+1)//2]
    print(dp[n])

if __name__ == '__main__':
    main()

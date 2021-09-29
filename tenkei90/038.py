def gcd(m,n):
    if n == 0:
        return m
    a = n
    b = m % n
    return gcd(a,b)


def main():
    A, B = map(int, input().split())
    m = max(A,B)
    n = min(A,B)
    a = gcd(m,n)
    ans = A * B // a
    if ans > 10**18:
        ans = 'Large'
    print(ans)


if __name__ == '__main__':
    main()

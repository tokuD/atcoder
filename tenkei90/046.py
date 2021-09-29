def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    a = [0 for i in range(46)]
    b = [0 for i in range(46)]
    c = [0 for i in range(46)]
    ans = 0

    for i in range(N):
        a[A[i]%46] += 1
        b[B[i]%46] += 1
        c[C[i]%46] += 1

    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i+j+k) % 46 == 0:
                    ans += a[i]*b[j]*c[k]
    print(ans)

if __name__ == '__main__':
    main()

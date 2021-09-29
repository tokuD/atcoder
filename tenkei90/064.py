def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    LRV = [list(map(int,input().split())) for i in range(Q)]
    dif = []
    ans = 0
    for i in range(N-1):
        dif.append(A[i+1]-A[i])
    for i in range(N-1):
        ans += abs(dif[i])
    for i in range(Q):
        L,R,V = map(lambda x: x-1,LRV[i])
        V += 1
        if L > 0:
            ans -= abs(dif[L-1])
            dif[L-1] += V
            ans += abs(dif[L-1])
        if R < N-1:
            ans -= abs(dif[R])
            dif[R] -= V
            ans += abs(dif[R])
        print(ans)

if __name__ == '__main__':
    main()

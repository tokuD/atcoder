def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(H)]
    B = [list(map(int,input().split())) for i in range(H)]
    C = [[0 for i in range(W)] for j in range(H)]
    ans = 0
    flag = True
    for i in range(H):
        for j in range(W):
            C[i][j] = B[i][j] - A[i][j]

    for i in range(H-1):
        for j in range(W-1):
            dif = C[i][j]
            C[i][j] -= dif
            C[i+1][j] -= dif
            C[i][j+1] -= dif
            C[i+1][j+1] -= dif
            ans += abs(dif)
    for i in range(H):
        for j in range(W):
            if C[i][j] != 0:
                flag = False

    if flag:
        print('Yes')
        print(ans)
    else:
        print('No')

if __name__ == '__main__':
    main()

def judge(ans,N,A,K):
    total = 0
    count = 0
    for i in range(N+1):
        if i == 0:
            total += A[i]
        else:
            total += A[i] - A[i-1]
        if total >= ans:
            total = 0
            count += 1
    if count >= K+1:
        return True
    else:
        return False



def main():
    N,L = map(int,input().split())
    K = int(input())
    A = list(map(int,input().split()))
    A.append(L)
    l = 1
    r = L
    while r-l>1:
        half = (r+l) // 2
        flag = judge(half,N,A,K)
        if flag:
            l = half
        else:
            r = half
    print(l)



if __name__ == '__main__':
    main()

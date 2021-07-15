
def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A.sort()
    B.sort()

    A_to_B = []
    total = 0
    ans = 0
    for i in range(N):
        b = B[i]
        if b > A[N-1]:
            total += N
        elif b < A[0]:
            pass
        else:
            start = 0
            end = N-1
            while end-start>1:
                mid = (start+end)//2
                if b <= A[mid]:
                    end = mid
                else:
                    start = mid
            total += end
        A_to_B.append(total)

    for i in range(N):
        c = C[i]
        if c > B[N-1]:
            ans += A_to_B[N-1]
            continue
        elif c < B[0]:
            continue
        else:
            start = 0
            end = N-1
            while end-start > 1:
                mid = (start+end)//2
                if c <= B[mid]:
                    end = mid
                else:
                    start = mid
            ans += A_to_B[end-1]
    print(ans)

if __name__ == "__main__":
    main()


def half_search(b,A,start,end):
    while end - start > 1:
        mid = (end+start)//2
        if b == A[mid]:
            return 0
        elif b < A[mid]:
            end = mid
        else:
            start = mid
    return min(abs(b-A[start]),abs(b-A[end]))




def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    B = [int(input()) for i in range(Q)]
    A.sort()
    ans = 0
    for i in range(Q):
        print(half_search(B[i],A,0,N-1))

if __name__ == '__main__':
    main()

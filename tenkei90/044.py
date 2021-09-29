from collections import deque

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    ans = []
    A = deque(A)
    for i in range(Q):
        T,x,y = map(int,input().split())
        if T == 1:
            A[x-1], A[y-1] = A[y-1], A[x-1]
        elif T == 2:
            a = A.pop()
            A.appendleft(a)
        elif T == 3:
            print(A[x-1])
            ans.append(A[x-1])

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()

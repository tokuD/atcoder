from ast import operator


def main():
    N = int(input())
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))
    S = [*S,*S,S[0]]
    T = [*T,*T,T[0]]

    for i in range(2*N):
        T[i+1] = min(T[i+1],T[i]+S[i])

    for i in range(N):
        if i == 0:
            print(T[-1])
        else:
            print(T[N+i])


if __name__ == '__main__':
    main()

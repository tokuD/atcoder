def main():
    N = int(input())
    S = list(input())
    ans = N*(N-1)//2
    kaburi = []
    a = 1
    pre = S[0]
    S.append(1)
    for i in range(1,N+1):
        # print(S[i],pre)
        if S[i] == pre:
            a += 1
        else:
            if 1 < a:
                kaburi.append(a)
                a = 1
        pre = S[i]

    for i in range(len(kaburi)):
        ai = kaburi[i]
        ans -= ai*(ai-1)//2
    print(ans)

if __name__ == '__main__':
    main()

def main():
    N,K = map(int,input().split())
    AB = [list(map(int,input().split())) for i in range(N)]
    score = []
    for i in range(N):
        a = AB[i][0]
        b = AB[i][1]
        score.append(a-b)
        score.append(b)
    score.sort(reverse=True)
    ans = sum(score[:K])
    print(ans)

if __name__ == '__main__':
    main()


def main():
    N, M = map(int,input().split())
    ans = [0 for i in range(N)]

    for i in range(M):
        a,b = map(int,input().split())
        ans[max(a,b)-1] += 1

    print(ans.count(1))

main()

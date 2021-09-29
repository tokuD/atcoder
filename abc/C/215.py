from itertools import permutations

def main():
    S,K = input().split()
    K = int(K)
    n = len(S)
    ans = []
    for i in permutations(S):
        ans.append(i)
    ans = set(ans)
    ans = sorted(ans)
    answer = ans[K-1]
    for i in range(len(answer)-1):
        print(answer[i],end='')
    print(answer[-1])


if __name__ == '__main__':
    main()

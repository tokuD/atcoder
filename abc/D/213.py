def tansaku(tree, ans=[], i=1):
    N = len(tree)
    root = tree[i]
    root.sort()
    if len(root[i]) < 1:
        return
    for j in range(len(root)):
        ans.append(root[j])
        return tansaku(tree,ans,root[j])



def main():
    N = int(input())
    AB = [list(map(int,input().split())) for i in range(N-1)]
    tree = [[] for i in range(N+1)]
    ans = [1]
    for i in range(N-1):
        a,b = AB[i]
        tree[a].append(b)
        tree[b].append(a)

    for i in range(1,N+1):
        tree[i].sort()
        for


if __name__ == '__main__':
    main()

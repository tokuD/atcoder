H,W = map(int, input().split())
G = [list(input()) for _ in range(H)]

ans = 'Yes'

for i in range(H):
    for j in range(W):

        if G[i][j] == '.':
            continue

        if i+1<H:
            if G[i+1][j] == '#':
                continue

        if 0<=i-1:
            if G[i-1][j] == '#':
                continue

        if j+1<W:
            if G[i][j+1] == '#':
                continue

        if 0<=j-1:
            if G[i][j-1] == '#':
                continue
        ans = 'No'

print(ans)
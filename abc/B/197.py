H,W,X,Y = map(int, input().split())
X -= 1
Y -= 1
G = [list(input()) for _ in range(H)]

ans = 0

#* (i,j)からp方向に進む
def dfs(i,j,p):

    #* 壁or障害物ならストップ
    if not (0<=i<H and 0<=j<W):
        return
    if G[i][j] == '#':
        return

    global ans
    ans += 1

    if p == 0:
        dfs(i+1,j,0)
    if p == 1:
        dfs(i-1,j,1)
    if p == 2:
        dfs(i,j+1,2)
    if p == 3:
        dfs(i,j-1,3)

for p in range(4):
    dfs(X,Y,p)

print(ans-3)
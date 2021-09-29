import sys
sys.setrecursionlimit(10**6)

N = int(input())

ans = 0
#*深さ優先探索
def dfs(x,y,a=False,b=False,c=False):
    """
    x:元の数
    y:追加する数
    a,b,c: 3,5,7のflag
    """

    #* xの1桁目にyを追加
    x = 10 * x + y

    #* Nを超えたら終了
    if x > N:
        return

    #* 3,5,7があればansに+1
    if a and b and c:
        global ans
        ans += 1

    #* 1桁目に3,5,7を追加
    dfs(x,3,a=True,b=b,c=c)
    dfs(x,5,a=a,b=True,c=c)
    dfs(x,7,a=a,b=b,c=True)

dfs(0, 0)
print(ans)

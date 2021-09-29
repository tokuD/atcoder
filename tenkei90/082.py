def f(x):
    left,right,keta = 1,10,1 #!(left,right]
    res = 0
    mod = 10**9 + 7
    while True:
        right = min(right,x+1)
        res += keta*(left+right-1)*(right-left) // 2
        if right == x+1:
            return res
        res %= mod
        left *= 10
        right *= 10
        keta += 1

def main():
    mod = 10**9+7
    L,R = map(int,input().split())
    ans = f(R) - f(L-1)
    print(ans % mod)

if __name__ == '__main__':
    main()

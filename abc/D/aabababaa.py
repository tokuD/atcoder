A, B, K = map(int, input().split())

#!二項係数
def comb(n, r):
    ans = 1
    bunsi = 1
    for i in range(r):
        ans *= n-i
        bunsi *= i+1
    return int(ans/bunsi)

ans = ''

while True:
    #!AかBの値が0になったら残りの文字は自動的に決まる
    if A==0:
        ans += 'b'*B
        break
    if B==0:
        ans += 'a'*A
        break

    #!先頭の文字はどっち
    if K <= comb(A+B-1, A-1):
        ans += 'a'
        A -= 1
    else:
        ans += 'b'
        K -= 1

print(ans)

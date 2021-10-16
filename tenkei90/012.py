H,W = map(int, input().split())
Q = int(input())
G = [[False]*W for _ in range(H)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r,c = map(lambda x:x-1, q[1:])
        G[r][c] = True
    else:
        
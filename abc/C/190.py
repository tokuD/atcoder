N,M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]
ans = 0
for i in range(2**K):
    plate = [False]*N
    tmp = 0
    for j in range(K):
        #* 1ならC,0ならD
        c,d = map(lambda x:x-1, CD[j])
        if (i >> j) & 1:
            plate[c] = True
        else:
            plate[d] = True
    for j in range(M):
        a,b = map(lambda x:x-1, AB[j])
        if plate[a] and plate[b]:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
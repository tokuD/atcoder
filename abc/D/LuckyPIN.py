N = int(input())
S = list(map(int, list(input())))
ans = 0
a = [[] for _ in range(10)]
for i in range(N):
    a[S[i]].append(i)

#! password = 'ijk'
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            flag = True
            if (a[i] != []) and (a[j] != []) and (a[k] != []) and flag:#! 全数字とりあえずあり
                l = a[i][0]
                for m in a[j]:
                    if m > l and flag:#! 2文字目が1文字目より後に出てくる
                        if a[k][-1] > m and flag: #! 3文字目の1番遅いのが2文字目より後ならOK
                            ans += 1
                            flag = False
                            # print(i,j,k)

print(ans)

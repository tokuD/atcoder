import heapq
N,M = map(int, input().split())
A = [list(input()) for _ in range(2*N)]

# #* 順位表,[得点,番号]
Q = [[] for _ in range(M+1)]
for i in range(2*N):
    Q[0].append([0,i])

for i in range(M):
    Q[i].sort(key=lambda x:(x[0],x[1]))
    for j in range(0,2*N,2):
        pa,a = Q[i][j]
        pb,b = Q[i][j+1]

        if A[a][i] == 'G':
            if A[b][i] == 'P':
                Q[i+1].append([pb-1,b])
                Q[i+1].append([pa,a])
            elif A[b][i] == 'C':
                Q[i+1].append([pb,b])
                Q[i+1].append([pa-1,a])
            else:
                Q[i+1].append([pb,b])
                Q[i+1].append([pa,a])

        if A[a][i] == 'P':
            if A[b][i] == 'C':
                Q[i+1].append([pb-1,b])
                Q[i+1].append([pa,a])
            elif A[b][i] == 'G':
                Q[i+1].append([pb,b])
                Q[i+1].append([pa-1,a])
            else:
                Q[i+1].append([pb,b])
                Q[i+1].append([pa,a])

        if A[a][i] == 'C':
            if A[b][i] == 'G':
                Q[i+1].append([pb-1,b])
                Q[i+1].append([pa,a])
            elif A[b][i] == 'P':
                Q[i+1].append([pb,b])
                Q[i+1].append([pa-1,a])
            else:
                Q[i+1].append([pb,b])
                Q[i+1].append([pa,a])

Q[-1].sort(key=lambda x:(x[0],x[1]))
for i in range(2*N):
    a,b = Q[-1][i]
    print(b+1)
# print(Q)


N = int(input())
S = list(input())
Q = int(input())
TAB = [list(map(int,input().split())) for _ in range(Q)]
S = [*S,*S[:N]] #* Sの前半を後ろにつける
start = 0 #* start位置の管理(0 or N)

for i in range(Q):
    T,A,B = TAB[i]
    if T == 1:
        a,b = S[start+A-1],S[start+B-1]
        S[start+A-1],S[start+B-1] = b,a
        if start+A+2*N-1 < 3*N:
            S[start+A+2*N-1] = b
        if start+B+2*N-1 < 3*N:
            S[start+B+2*N-1] = a
        if start+A-2*N-1 >= 0:
            S[start+A-2*N-1] = b
        if start+B-2*N-1 >= 0:
            S[start+B-2*N-1] = a
    if T == 2:
        if start == 0:
            start = N
        else:
            start = 0
    # print(S,start)

print(''.join(S[start:start+2*N]))
# print(S)

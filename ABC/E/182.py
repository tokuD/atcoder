# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    H,W,N,M = map(int, input().split())
    row = [[0,W+1] for _ in range(H+2)]
    column = [[0,H+1] for _ in range(W+2)]
    G = [[0]*(W+2) for _ in range(H+2)] #* 電球1、ブロック2
    for _ in range(N):
        a,b = map(int, input().split())
        G[a][b] = 1
        row[a].append(b)
        column[b].append(a)

    for _ in range(M):
        c,d = map(int, input().split())
        G[c][d] = 2
        row[c].append(d)
        column[d].append(c)

    for r in row:
        r.sort()

    for c in column:
        c.sort()

    #* 各マスについて4方向を見て、ブロックと電球のどちらが近いか調べる
    #* 1方向でも電球が近ければ、答えに追加
    ans = 0
    for i in range(1,H+1):
        for j in range(1,W+1):
            if G[i][j] == 2: continue
            if G[i][j] == 1:
                ans += 1
                continue

            a = bisect_left(column[j],i)
            b = bisect_left(row[i],j)
            i0 = column[j][a]
            i1 = column[j][a-1]
            j0 = row[i][b]
            j1 = row[i][b-1]
            if G[i0][j] == 1 or G[i1][j] == 1 or G[i][j0] == 1 or G[i][j1] == 1:
                ans += 1
                # print('------------')
                # print(i,j)
                # print(a,b)
            # else:

    print(ans)
    # for r in row[1:-1]:
    #     print(r)

    # print('------------')
    # for c in column[1:-1]:
    #     print(c)


if __name__ == '__main__':
    main()
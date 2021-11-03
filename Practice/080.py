# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    H,W,K,V = map(int, input().split())
    A = [[0]*(W+1) for _ in range(H+1)]
    for i in range(1,H+1):
        a = [0] + list(map(int, input().split()))
        for j in range(1,W+1):
            A[i][j] = a[j]
    cnt = [[0]*(W+1) for _ in range(H+1)]
    for i in range(1,H+1):
        for j in range(1,W+1):
            cnt[i][j] = A[i][j] + cnt[i-1][j] + cnt[i][j-1] - cnt[i-1][j-1]

    ans = 0
    ok = 0
    ng = H*W+1
    # while ng-ok>1:
    #     S = (ok+ng)//2
    for S in range(1,H*W+1):
        money = V - S*K
        flag = False
        for di in range(1,H+1):
            if S % di != 0: continue
            dj = S // di
            di -= 1
            dj -= 1
            for i in range(1,H+1-di):
                for j in range(1,W+1-dj):
                    value = cnt[i+di][j+dj] - cnt[i+di][j-1] - cnt[i-1][j+dj] + cnt[i-1][j-1]
                    if money >= value:
                        flag = True
        if flag:
            ok = S
            ans = S
        else:
            ng = S

    # print(ok)
    print(ans)

if __name__ == '__main__':
    main()
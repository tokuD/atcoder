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
    N,M,Q = map(int, input().split())
    cnt = [[0]*(N+1) for _ in range(N+1)] #* cnt[i][j]:区間[i,j]の列車の台数
    for _ in range(M):
        l,r = map(int, input().split())
        cnt[l][r] += 1
    for i in range(N+1):
        for j in range(N+1):
            if i > 0: cnt[i][j] += cnt[i-1][j]
            if j > 0: cnt[i][j] += cnt[i][j-1]
            if i > 0 and j > 0: cnt[i][j] -= cnt[i-1][j-1]

    ans = []
    for _ in range(Q):
        p,q = map(int, input().split())
        res = cnt[q][q]
        if p > 0:
            res += -cnt[p-1][q] - cnt[q][p-1] + cnt[p-1][p-1]
        ans.append(res)

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
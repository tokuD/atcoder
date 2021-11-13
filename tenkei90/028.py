# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N = int(input())
    ma = 10**3+2
    cnt = [[0]*(ma) for _ in range(ma)]
    for _ in range(N):
        lx,ly,rx,ry = map(int, input().split())
        cnt[ly][lx] += 1
        cnt[ry][rx] += 1
        cnt[ry][lx] -= 1
        cnt[ly][rx] -= 1

    for i in range(ma):
        for j in range(1,ma):
            cnt[i][j] += cnt[i][j-1]

    for j in range(ma):
        for i in range(1,ma):
            cnt[i][j] += cnt[i-1][j]

    ans = [0]*(N+1)
    for i in range(ma-1):
        for j in range(ma-1):
            k = cnt[i][j]
            ans[k] += 1

    for a in ans[1:]:
        print(a)

if __name__ == '__main__':
    main()
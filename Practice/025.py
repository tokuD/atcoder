# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
sys.setrecursionlimit(10**5)


def dfs(i, j, h, w, dx, dy, visited, CW):
    if visited[i][j]:
        return
    visited[i][j] = True

    for dj,di in zip(dx,dy):
        if 0<= i+di < h and 0<= j+dj < w:
            if CW[i+di][j+dj]:
                dfs(i+di,j+dj,h,w,dx,dy,visited,CW)


def main():
    ans = []
    wh = []
    CW = []
    while True:
        w,h = map(int, input().split())
        if w == 0 and h == 0:
            break
        cw = [list(map(int, input().split())) for _ in range(h)]
        wh.append((w,h))
        CW.append(cw)

    for i in range(len(wh)):
        w,h = wh[i]
        cw = CW[i]
        dx = [0,1,1,1,0,-1,-1,-1]
        dy = [1,1,0,-1,-1,-1,0,1]
        visited = [[False]*w for _ in range(h)]
        res = 0
        for i in range(h):
            for j in range(w):
                if cw[i][j]:
                    if visited[i][j]:
                        continue
                    res += 1
                    dfs(i,j, h, w, dx, dy, visited, cw)

        ans.append(res)

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)


def main():
    DX = [1,-1,0,0]
    DY = [0,0,1,-1]
    R,C = map(int, input().split())
    sy,sx = map(lambda x:int(x)-1, input().split())
    gy,gx = map(lambda x:int(x)-1, input().split())
    G = [list(input()) for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    Q = deque()
    Q.append((sy,sx,0))
    ans = 0
    while len(Q) > 0:
        y,x,dis = Q.popleft()
        if visited[y][x]:
            continue
        if (y,x) == (gy,gx):
            ans = dis
        visited[y][x] = True
        for dx,dy in zip(DX,DY):
            if G[y+dy][x+dx] == '.':
                Q.append((y+dy,x+dx,dis+1))

    print(ans)


if __name__ == '__main__':
    main()
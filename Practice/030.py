#? from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

dxdy = [(1,0),(-1,0),(0,1),(0,-1)]


def main():
    H,W,N = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    start = [(0,0) for _ in range(N+1)]
    for y in range(H):
        for x in range(W):
            s = G[y][x]
            if s in ['X','.']:
                continue
            if s == 'S':
                start[0] = (y,x)
            else:
                start[int(s)] = (y,x)

    ans = 0

    for i in range(N):
        sy,sx = start[i]
        gy,gx = start[i+1]
        Q = deque()
        Q.append((sy,sx,0))
        visited = [[False]*W for _ in range(H)]
        while len(Q) > 0:
            y,x,dis = Q.popleft()
            if visited[y][x]:
                continue
            if (y,x) == (gy,gx):
                ans += dis
                break
            visited[y][x] = True

            for dx,dy in dxdy:
                if not (0<=x+dx<W and 0<=y+dy<H): continue
                if G[y+dy][x+dx] == 'X': continue
                Q.append((y+dy,x+dx,dis+1))

    print(ans)

if __name__ == '__main__':
    main()
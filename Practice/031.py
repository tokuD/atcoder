# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    X,Y = map(int, input().split())
    G = []
    G.append([0]*(X+2))
    for _ in range(Y):
        r = [0] + list(map(int, input().split())) + [0]
        G.append(r)
    G.append([0]*(X+2))
    dxdy1 = [(-1,0),(0,-1),(1,-1),(1,0),(1,1),(0,1)]
    dxdy0 = [(-1,0),(-1,-1),(0,-1),(1,0),(0,1),(-1,1)]
    visited = [[False]*(X+2) for _ in range(Y+2)]
    ans = 0
    Q = deque()
    #* Q[y,x]
    Q.appendleft((0,0))
    while len(Q) > 0:
        y,x = Q.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True
        if y % 2 == 1:
            for dx,dy in dxdy1:
                if not (0<=x+dx<X+2 and 0<=y+dy<Y+2): continue
                if G[y+dy][x+dx] == 1:
                    ans += 1
                    continue
                Q.append((y+dy,x+dx))
        else:
            for dx,dy in dxdy0:
                if not (0<=x+dx<X+2 and 0<=y+dy<Y+2): continue
                if G[y+dy][x+dx] == 1:
                    ans += 1
                    continue
                Q.append((y+dy,x+dx))

    print(ans)

if __name__ == '__main__':
    main()
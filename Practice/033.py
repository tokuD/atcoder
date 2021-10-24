# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
    Y,X = map(int, input().split())
    white = 0
    min_dis = -1
    G = []
    for _ in range(Y):
        S = list(input())
        white += S.count('.')
        G.append(S)

    visited = [[False]*X for _ in range(Y)]
    Q = deque()
    #* (y,x,dis)
    Q.append((0,0,1))
    while len(Q) > 0:
        y,x,dis = Q.popleft()
        if visited[y][x]:
            continue
        if (y,x) == (Y-1,X-1):
            min_dis = dis
            break
        visited[y][x] = True
        for dx,dy in dxdy:
            if not (0<=x+dx<X and 0<=y+dy<Y): continue
            if G[y+dy][x+dx] == '#': continue
            Q.append((y+dy,x+dx,dis+1))

    if min_dis == -1:
        print(-1)
    else:
        print(white-min_dis)

if __name__ == '__main__':
    main()
# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

dxdy = [(1,0),(-1,0),(0,1),(0,-1)]

def get():
    X,Y = map(int, input().split())
    #* wall[(y0,x0,y1,x1)] の間に壁がある
    wall = set()
    for y in range(2*Y-1):
        q = list(map(int, input().split()))
        for x in range(len(q)):
            if q[x] == 0: continue
            if y % 2 == 0:
                wall.add((y//2,x,y//2,x+1))
            else:
                wall.add((y//2,x,y//2+1,x))

    return [X,Y,wall]

def search(X:int, Y:int, wall)->int:
    res = 0
    visited = [[False]*X for _ in range(Y)]
    Q = deque()
    #* (y,x,dis)
    Q.append((0,0,1))
    while len(Q) > 0:
        y,x,dis = Q.popleft()
        if visited[y][x]:
            continue
        if (y,x) == (Y-1,X-1): res = dis
        visited[y][x] = True
        for dx,dy in dxdy:
            if not (0<=x+dx<X and 0<=y+dy<Y): continue
            x0 = min(x,x+dx)
            x1 = max(x,x+dx)
            y0 = min(y,y+dy)
            y1 = max(y,y+dy)
            if (y0,x0,y1,x1) in wall: continue
            Q.append((y+dy,x+dx,dis+1))

    return res

def main():

    ans = []

    while True:
        X,Y,wall = get()
        if (X,Y) == (0,0):
            break
        ans.append(search(X,Y,wall))

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
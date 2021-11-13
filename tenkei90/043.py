# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set,Deque
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
sys.setrecursionlimit(10**5)

def dfs(h:int, w:int, dx:int, dy:int, now:int, G:List[List[str]], count:List[List[int]], H:int, W:int, Q:Deque[Tuple[int]]):

    h += dy
    w += dx
    if not (0<=h<H and 0<=w<W): return
    if G[h][w] == '#': return
    if count[h][w] < now: return
    count[h][w] = now
    Q.append((h,w))
    dfs(h,w,dx,dy,now,G,count,H,W,Q)


def main():
    INF = 10**20
    dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
    H,W = map(int, input().split())
    hs,ws = map(lambda x:int(x)-1, input().split())
    hg,wg = map(lambda x:int(x)-1, input().split())
    G = []
    for _ in range(H):
        S = list(input().rstrip())
        G.append(S)

    Q = deque()
    Q.append((hs,ws))
    visited = [[False]*W for _ in range(H)]
    count = [[INF]*W for _ in range(H)]
    count[hs][ws] = -1

    while len(Q)>0:
        h,w = Q.popleft()
        if visited[h][w]: continue
        visited[h][w] = True
        now = count[h][w] + 1
        for dx,dy in dxdy:
            dfs(h,w,dx,dy,now,G,count,H,W,Q)

    print(count[hg][wg])

if __name__ == '__main__':
    main()
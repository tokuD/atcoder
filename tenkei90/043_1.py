# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set,Deque
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    INF = 10**20
    dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
    H,W = map(int, input().split())
    rs,cs = map(lambda x:int(x)-1, input().split())
    rt,ct = map(lambda x:int(x)-1, input().split())
    G = []
    for i in range(H):
        S = list(input().rstrip())
        for s in S:
            G.append(s)

    dp = [[INF]*4 for _ in range(H*W)]
    dp[rs*W+cs] = [0,0,0,0]
    Q = deque()
    for i in range(4):
        Q.append((rs,cs,i))
    visited = [[False]*4 for _ in range(H*W)]
    while len(Q)>0:
        i,j,d = Q.popleft()
        curr = i*W+j
        if visited[curr][d]: continue
        visited[curr][d] = True
        for l in range(4):
            dx,dy = dxdy[l]
            if not (0<=i+dy<H): continue
            if not (0<=j+dx<W): continue
            nxt = (i+dy)*W+j+dx
            if G[nxt]=='#': continue
            if visited[nxt][l]: continue
            if d==l:
                if dp[nxt][l] > dp[curr][d]:
                    dp[nxt][l] = dp[curr][d]
                    Q.appendleft((i+dy,j+dx,l))
            else:
                if dp[nxt][l] > dp[curr][d]+1:
                    dp[nxt][l] = dp[curr][d]+1
                    Q.append((i+dy,j+dx,l))

    print(min(dp[rt*W+ct]))

if __name__ == '__main__':
    main()
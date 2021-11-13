# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

class UnionFind():

    def __init__(self, N:int):
        self.par = [i for i in range(N)]
        self.size = [1]*N
        self.marked = [False]*N

    def root(self, x:int):
        if self.par[x] == x: return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x:int, y:int):
        rx, ry = self.root(x), self.root(y)
        if rx == ry: return
        if self.size[rx] >= self.size[ry]:
            self.par[ry] = rx
            self.size[rx] += self.size[ry]
        else:
            self.par[rx] = ry
            self.size[ry] += self.size[rx]

    def issame(self, x:int, y:int):
        if not self.marked[x]: return False
        if not self.marked[y]: return False
        return self.root(x) == self.root(y)

def main():
    dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
    H,W = map(int, input().split())
    Q = int(input())
    unionfind = UnionFind(H*W)
    ans = []
    for _ in range(Q):
        q = list(map(lambda x:int(x)-1, input().split()))
        if q[0] == 0:
            r,c = q[1:]
            unionfind.marked[W*r+c] = True
            for dx,dy in dxdy:
                i,j = r+dx,c+dy
                if 0<=i<H and 0<=j<W:
                    if unionfind.marked[W*i+j]:
                        unionfind.unite(W*r+c, W*i+j)
        else:
            ra,ca,rb,cb = q[1:]
            if unionfind.issame(W*ra+ca, W*rb+cb):
                ans.append('Yes')
            else:
                ans.append('No')

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
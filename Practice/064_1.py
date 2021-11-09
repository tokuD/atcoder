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

    def __init__(self,N:int):
        self.par = [-1]*N
        self.size = [1]*N

    def root(self, x:int):
        """
        xの親をたどっていき、根にたどり着いたらそれを返す
        道中で通った点は親を根に変えておく
        """
        if self.par[x] == -1: return x
        self.par[x] = self.root(self.par[x])
        self.size[x] = 1
        return self.par[x]

    def unite(self, x:int, y:int):
        """
        xのグループとyのグループを併合する
        その際、サイズが小さい方の根を大きい方の根につける
        """
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False
        if self.size[rx] >= self.size[ry]:
            self.par[ry] = rx
            self.size[rx] += self.size[ry]
        else:
            self.par[rx] = ry
            self.size[ry] += self.size[rx]
        return True

#! プリム法
def main():
    V,E = map(int, input().split())
    edges = []
    for _ in range(E):
        s,t,w = map(int, input().split())
        edges.append((w,s,t))
    edges.sort()

    unionfind = UnionFind(V)

    ans = 0
    for w,s,t in edges:
        if unionfind.unite(s,t):
            ans += w

    print(ans)

if __name__ == '__main__':
    main()
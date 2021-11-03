# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

class UnionFind():

    def __init__(self, N:int, W:List[int]):
        self.child = [[] for _ in range(N)] #* 頂点iの子
        self.par = [-1] * N #* 頂点iの親
        self.size = [1] * N #* 頂点iを根とする部分木が含む頂点数
        self.weight = W #* 頂点iをねとする部分木の重さ
        return

    def root(self, i:int):
        """
        頂点iの根を返す
        その過程で通った頂点を、直接根に繋ぐ
        """
        if self.par[i] == -1: return i
        self.par[i] = self.root(self.par[i])
        return self.par[i]

    def unite(self, x:int, y:int):
        """
        頂点xを含む木と頂点yを含む木を併合する
        その際、頂点数が多い方を根にする
        """
        rx,ry = self.root(x), self.root(y)
        if rx == ry: return
        if self.size[rx] >= self.size[ry]:
            self.par[ry] = rx
            self.size[rx] += self.size[ry]
            self.weight[rx] += self.weight[ry]
        else:
            self.par[rx] = ry
            self.size[ry] += self.size[rx]
            self.weight[ry] += self.weight[rx]
        return

    def issame(self, x:int, y:int):
        """頂点xと頂点yの根が同じかどうか"""
        return self.root(x) == self.root(y)

def main():
    N,Q = map(int, input().split())
    W = list(map(int, input().split()))
    clay = UnionFind(N, W)
    ans = []
    for _ in range(Q):
        t,x,y = map(int, input().split())
        if t == 0:
            clay.unite(x, y)
        else:
            rx = clay.root(x)
            ans.append(clay.weight[rx])

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
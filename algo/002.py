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

    def __init__(self, N:int):
        self.child = [[] for _ in range(N)] #* child[i]:頂点iの子
        self.par = [-1] * N #* par[i]:頂点iの親

    def root(self, i:int):
        """頂点iの根を探し、途中の頂点を根に直接つなぐ"""
        if self.par[i] == -1: return i
        self.par[i] = self.root(self.par[i])
        return self.par[i]

    def unite(self, x:int, y:int):
        """
        頂点iを含む木と頂点jを含む木を併合する
        併合の際は、頂点番号が小さい方を根とする
        """
        a,b = self.root(x), self.root(y)
        if a == b: return
        if a < b: #* bの親をaにする
            self.par[b] = a
        else:
            self.par[a] = b

class UnionFind():

    def __init__(self,n):
        self.par = [-1] * n #* par[i]:要素iの親
        self.rank = [0] * n #* rank[i]:要素iが属する木の高さ
        self.siz = [-1] * n #* siz[i]:要素iが属する木の頂点数

    def root(self, x):
        """xの根を求める"""
        if self.par[x] == -1: return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def issame(self, x, y):
        """xとyが同じグループに属するか"""
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        """xを含むグループとyを含むグループを併合する"""
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return
        if self.rank[rx] < self.rank[ry]:
            rx,ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]

    def size(self, x):
        return siz[root(x)]

def main():
    N,M = map(int, input().split())
    unionfind = UnionFind(N)
    for _ in range(M):
        a,b = map(int, input().split())
        unionfind.unite(a, b)

    for k in range(N):
        print(unionfind.root(k))


if __name__ == '__main__':
    main()
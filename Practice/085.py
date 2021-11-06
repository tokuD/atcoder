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

    def __init__(self, n:int):
        self.par = [-1]*n #* i番目の要素の親
        self.size = [1]*n #* i番目を頂点とする部分木の要素数

    def root(self,x):
        """
        xを含むグループの根を返す
        途中で通った点は直接根に繋いでおく
        """
        if self.par[x] == -1: return x
        self.par[x] = self.root(self.par[x])
        self.size[x] = 1
        return self.par[x]

    def unite(self,x,y):
        """xを含むグループとyを含むグループを併合する"""
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return
        #* サイズが小さい方を大きい方の根に繋ぐ
        if self.size[rx] >= self.size[ry]:
            self.par[ry] = rx
            self.size[rx] += self.size[ry]
        else:
            self.par[rx] = ry
            self.size[ry] += self.size[rx]

    def issame(self,x,y):
        """xとyが同じグループかを調べる"""
        return self.root(x) == self.root(y)


def main():
    N,Q = map(int, input().split())
    group = UnionFind(N)
    ans = []
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 0:
            group.unite(q[1],q[2])
        else:
            if group.issame(q[1],q[2]):
                ans.append(1)
            else:
                ans.append(0)

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
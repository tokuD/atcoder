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
        self.par = [-1] * N
        self.size = [1] * N

    def root(self, x:int):
        """
        頂点xの根を返す
        通った頂点は直接根につなぐ
        """
        if self.par[x] == -1: return x
        self.par[x] = self.root(self.par[x])
        self.size[x] = 1
        return self.par[x]

    def unite(self, x:int, y:int):
        """
        xを含むグループとyを含むグループを併合
        その際、サイズの大きい方を根とする
        """
        rx, ry = self.root(x), self.root(y)
        if rx == ry: return 0
        size_x = self.size[rx]
        size_y = self.size[ry]
        if self.size[rx] >= self.size[ry]:
            self.par[ry] = rx
            self.size[rx] += self.size[ry]
        else:
            self.par[rx] = ry
            self.size[ry] += self.size[rx]
        return size_x * size_y


def main():
    N,M = map(int, input().split())
    AB = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
    ans = []
    now = N*(N-1)//2
    group = UnionFind(N)
    for i in range(M)[::-1]:
        a,b = AB[i]
        ans.append(now)
        now -= group.unite(a,b)

    for a in ans[::-1]:
        print(a)


if __name__ == '__main__':
    main()
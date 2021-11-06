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
        途中で通った点は根につなぎ、サイズを1に
        """
        if self.par[x] == -1: return x
        self.par[x] = self.root(self.par[x])
        self.size[x] = 1
        return self.par[x]

    def unite(self, x:int, y:int):
        """
        xを含むグループとyを含むグループを併合する
        その際、サイズが小さい方が子になるようにする
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

    def issame(self, x:int, y:int):
        return self.root(x) == self.root(y)

def main():
    N,M = map(int, input().split())
    ans = 0
    AB = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
    #* 各辺を取り除いた場合に連結かどうか確かめる
    for i in range(M):
        group = UnionFind(N)
        flag = False
        for j in range(M):
            if i == j: continue
            a,b = AB[j]
            group.unite(a,b)
        for i in range(1,N):
            if group.issame(0,i): continue
            flag = True
        if flag:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
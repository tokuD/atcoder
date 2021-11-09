# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
import heapq
# sys.setrecursionlimit(10**5)

# class UnionFind():

#     def __init__(self, N:int):
#         self.par = [-1]*N
#         self.size = [1]*N

#     def root(self, x:int):
#         if self.par[x] == -1: return x
#         self.par[x] = self.root(self.par[x])
#         self.size[x] = 1
#         return self.par[x]

#     def unite(self, x:int, y:int):
#         rx,ry = self.root(x), self.root(y)
#         if rx == ry: return False
#         if self.size[rx] >= self.size[ry]:
#             self.par[ry] = rx
#             self.size[rx] += self.size[ry]
#         else:
#             self.par[rx] = ry
#             self.size[ry] += self.size[rx]
#         return True

# #! クラスカル法
# def main():
#     N,M,K = map(int, input().split())
#     edges = []
#     for _ in range(M):
#         a,b,c = map(int, input().split())
#         a -= 1
#         b -= 1
#         edges.append((c,a,b))
#     edges.sort()
#     unionfind = UnionFind(N)
#     ans = 0
#     used = []
#     for c,a,b in edges:
#         if unionfind.unite(a,b):
#             ans += c
#             used.append(c)

#     for i in range(1,K):
#         ans -= used[-i]

#     print(ans)

#! プリム法
def main():
    N,M,K = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a,b,c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((c,b))
        G[b].append((c,a))

    ans = 0
    used = []

    marked = [False]*N
    Q = [] #* (通行料金,都市)
    heapq.heappush(Q,(0,0))
    while len(Q)>0:
        fee,curr = heapq.heappop(Q)
        if marked[curr]: continue
        marked[curr] = True
        ans += fee
        used.append(fee)
        for nxt_fee,nxt in G[curr]:
            if marked[nxt]: continue
            heapq.heappush(Q, (nxt_fee,nxt))

    used.sort()
    for i in range(1,K):
        ans -= used[-i]

    print(ans)

if __name__ == '__main__':
    main()
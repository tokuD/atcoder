# from __future__ import annotations
from typing import List,Union,Tuple
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
import heapq
# sys.setrecursionlimit(10**5)

def solve(a:int, b:int, G:List[List[Tuple[int]]], N:int):
    cost = [-1]*N
    Q = []
    heapq.heappush(Q,(0,a))
    while len(Q)>0:
        now_cost, curr = heapq.heappop(Q)
        if cost[curr] != -1: continue
        cost[curr] = now_cost
        for nxt,nxt_cost in G[curr]:
            heapq.heappush(Q,(now_cost+nxt_cost, nxt))
    return cost[b]

def main():
    N,K = map(int, input().split())
    G = [[] for _ in range(N)] #* G[i]:(頂点iから行ける都市,その運賃)
    ans = []
    for _ in range(K):
        q = list(map(lambda x:int(x)-1, input().split()))
        if q[0] == -1:
            a,b = q[1:]
            ans.append(solve(a,b,G,N))
        else:
            c,d,e = q[1:]
            G[c].append((d,e+1))
            G[d].append((c,e+1))

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
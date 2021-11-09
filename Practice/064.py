# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
import heapq
# sys.setrecursionlimit(10**5)

#! プリム法
def main():
    V,E = map(int, input().split())
    G = [[] for _ in range(V)]
    for _ in range(E):
        s,t,w = map(int, input().split())
        G[s].append((t,w))
        G[t].append((s,w))
    Q = [] #* (weight, node)
    heapq.heappush(Q,(0,0))
    marked = [False]*V
    ans = 0
    while len(Q)>0:
        w,n = heapq.heappop(Q)
        if marked[n]: continue
        marked[n] = True
        ans += w
        for nxt,nxt_w in G[n]:
            if marked[nxt]: continue
            heapq.heappush(Q, (nxt_w,nxt))

    print(ans)


if __name__ == '__main__':
    main()
#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
import heapq
# sys.setrecursionlimit(10**5)

def main():
    V,E,r = map(int,input().split())
    G = [[] for _ in range(V)] #* G[i]:頂点iから行ける都市
    for _ in range(E):
        s,t,d = map(int,input().split())
        G[s].append((t,d))
    distance = ['INF']*V
    Q = []
    heapq.heappush(Q,(0,r))
    while len(Q) > 0:
        dis,curr = heapq.heappop(Q)
        if distance[curr] != 'INF': continue
        distance[curr] = dis
        for nxt,d in G[curr]:
            heapq.heappush(Q,(dis+d,nxt))

    for d in distance:
        print(d)


if __name__ == '__main__':
    main()
# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)


def main():
    V,E = map(int, input().split())
    INF = 10 ** 20
    G = [[] for _ in range(V)] #* G[i]:頂点iから行ける都市とその距離
    for _ in range(E):
        s,t,d = map(int, input().split())
        G[s].append((t,d))
    dp = [[INF]*V for _ in range(2**V)] #* dp[i][j]:今まで通った頂点がj,前の頂点がi
    dp[0][0] = 0

    for bit in range(2**V):
        for s in range(V):
            for t,d in G[s]:
                if (bit >> t) & 1 == 1: continue
                dp[bit|(1<<t)][t] = min(dp[bit|(1<<t)][t], dp[bit][s]+d)

    if dp[-1][0] == INF:
        print(-1)
    else:
        print(dp[-1][0])


if __name__ == '__main__':
    main()
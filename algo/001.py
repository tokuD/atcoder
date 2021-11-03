# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
sys.setrecursionlimit(10**5)

def dfs(n, visited, G):
    if visited[n]: return
    visited[n] = True
    for chi in G[n]:
        if visited[chi]: continue
        dfs(chi, visited, G)

def main():
    N,M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a,b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    visited = [False]*N
    ans = 0

    for n in range(N):
        if visited[n]: continue
        ans += 1
        dfs(n, visited, G)

    print(ans)


if __name__ == '__main__':
    main()
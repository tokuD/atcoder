# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    INF = 10**20
    N,M = map(int, input().split())
    dis = [[INF]*N for _ in range(N)]
    for _ in range(M):
        a,b,t = map(int, input().split())
        a -= 1
        b -= 1
        dis[a][b] = t
        dis[b][a] = t
    for i in range(N):
        dis[i][i] = 0

    for k in range(N):
        for x in range(N):
            for y in range(N):
                if dis[x][k] == INF or dis[k][y] == INF: continue
                dis[x][y] = min(dis[x][y], dis[x][k]+dis[k][y])

    ans = INF
    for d in dis:
        res = 0
        for a in d:
            if a == INF: continue
            res = max(res,a)
        ans = min(ans,res)

    print(ans)

if __name__ == '__main__':
    main()
# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    mod = 998244353
    N,M = map(int, input().split())
    G = [[] for _ in range(N)] #* G[i]:頂点iからのびてる辺
    U = []
    V = []
    dp = [0]*N
    for i in range(M):
        u,v = map(lambda x:int(x)-1, input().split())
        G[u].append(i)
        G[v].append(i)
        U.append(u)
        V.append(v)

    used = [False]*M #* 使用済みの辺
    Q = deque()
    ans = 0
    for i in range(M):
        if used[i]: continue
        Q.append(i)
        dp[U[i]] = 1
        res = 0
        while len(Q)>0:
            edge = Q.popleft()
            if used[edge]: continue
            used[edge] = True
            u,v = U[edge],V[edge]
            dp[v] += dp[u]
            dp[v] %= mod
            res = max(res,dp[v])
            for nxt_edge in G[v]:
                if used[nxt_edge]: continue
                Q.append(nxt_edge)
        ans += res
        print(res,i)

    # print(ans)

if __name__ == '__main__':
    main()
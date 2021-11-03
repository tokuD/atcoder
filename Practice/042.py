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
    N,M = map(int, input().split())
    D = [0] + [int(input()) for _ in range(N)]
    C = [0] + [int(input()) for _ in range(M)]
    INF = 10**20
    dp = [[INF]*(N+1) for _ in range(M+1)]
    dp[0][0] = 0
    for m in range(M):
        for n in range(N+1):
            dp[m+1][n] = min(dp[m+1][n], dp[m][n])
            if n+1>N: continue
            dp[m+1][n+1] = min(dp[m+1][n+1], dp[m][n]+D[n+1]*C[m+1])

    ans = INF
    for m in range(1,M+1):
        ans = min(ans, dp[m][-1])

    print(ans)


if __name__ == '__main__':
    main()
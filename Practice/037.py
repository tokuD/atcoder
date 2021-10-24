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
    INF = 10 ** 20
    N,M = map(int, input().split())
    C = [0] + list(map(int, input().split()))
    dp = [[INF]*(N+1) for _ in range(M+1)]
    dp[0][0] = 0
    for m in range(1,M+1):
        for n in range(N+1):
            dp[m][n] = min(dp[m][n], dp[m-1][n])
            if n - C[m-1] >= 0: dp[m][n] = min(dp[m][n], dp[m-1][n-C[m-1]]+1)
            if n - C[m] >= 0: dp[m][n] = min(dp[m][n], dp[m][n-C[m]]+1)

    print(dp[-1][-1])


if __name__ == '__main__':
    main()
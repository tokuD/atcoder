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
    N = int(input())
    P = list(map(float, input().split()))

    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(N+1):
            dp[i][j] += dp[i-1][j]*(1-P[i-1])
            if j == 0: continue
            dp[i][j] += dp[i-1][j-1]*P[i-1]

    ans = sum(dp[N][N//2+1:])
    print(ans)

if __name__ == '__main__':
    main()
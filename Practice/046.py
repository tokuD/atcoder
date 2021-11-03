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
    N = int(input())
    P = []
    for i in range(N):
        a,b = map(int, input().split())
        if i == 0: P.append(a)
        P.append(b)
    INF = 10**20
    dp = [[INF]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0

    for d in range(1,N):
        for s in range(N-d):
            i = s
            j = s+d
            for k in range(i,j):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+P[i-1]*P[k]*P[j])

    print(dp[0][-1])

if __name__ == '__main__':
    main()
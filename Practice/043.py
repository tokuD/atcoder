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
    S = [[0] + list(input().rstrip()) for _ in range(5)]
    A = [[None]*5 for _ in range(N+1)]
    for i in range(5):
        for j in range(N+1):
            s = S[i][j]
            A[j][i] = s
    INF = 10**20
    dp = [[INF]*3 for _ in range(N+1)]
    cha = ['R','B','W']
    for i in range(3):
        dp[1][i] = 5 - A[1].count(cha[i])

    for i in range(1,N):
        for j in range(3):
            for k in range(3):
                if j == k: continue
                dp[i+1][k] = min(dp[i+1][k], dp[i][j]+5-A[i+1].count(cha[k]))

    ans = min(dp[-1])
    print(ans)

if __name__ == '__main__':
    main()
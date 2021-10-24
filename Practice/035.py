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
    N,W = map(int, input().split())
    vw = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [[-1]*(W+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(W+1):
            if dp[i][j] == -1: continue
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            v,w = vw[i]
            if j + w <= W:
                dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j]+v)

    ans = 0
    for v in dp[-1]:
        ans = max(ans,v)
    print(ans)



if __name__ == '__main__':
    main()
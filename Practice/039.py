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
    N -= 1
    S = [0] + list(map(int, input().split()))
    ans = S.pop()
    dp = [[0]*(21) for _ in range(N+1)]
    dp[1][S[1]] = 1

    #* 配るdp
    for i in range(1,N):
        for j in range(21):
            if dp[i][j] == 0: continue
            if j + S[i+1] <= 20: dp[i+1][j+S[i+1]] += dp[i][j]
            if j - S[i+1] >= 0: dp[i+1][j-S[i+1]] += dp[i][j]

    #* 貰うdp
    # for i in range(2,N+1):
    #     for j in range(21):
    #         if j + S[i] <= 20: dp[i][j] += dp[i-1][j+S[i]]
    #         if j - S[i] >= 0: dp[i][j] += dp[i-1][j-S[i]]

    print(dp[-1][ans])



if __name__ == '__main__':
    main()
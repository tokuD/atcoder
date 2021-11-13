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
    S = list(input().rstrip())
    T = list(input().rstrip())

    dp = [['']*(len(T)+1) for _ in range(len(S)+1)]

    for i in range(1,len(S)+1):
        for j in range(1,len(T)+1):
            if len(dp[i][j]) < len(dp[i-1][j]): dp[i][j] = dp[i-1][j]
            if len(dp[i][j]) < len(dp[i][j-1]): dp[i][j] = dp[i][j-1]
            if S[i-1] == T[j-1]:
                if len(dp[i][j]) < len(dp[i-1][j-1]) + 1:
                    dp[i][j] = dp[i-1][j-1] + S[i-1]

    print(dp[-1][-1])

if __name__ == '__main__':
    main()
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
    n = int(input())
    dp = [1]*(n+1)
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])


if __name__ == '__main__':
    main()
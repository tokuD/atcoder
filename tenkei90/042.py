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
    mod = 10**9+7
    K = int(input())
    if K % 9 != 0:
        print(0)
        exit()

    dp = [0]*(K+10)
    dp[0] = 1
    for i in range(K):
        for j in range(1,10):
            dp[i+j] += dp[i]
            dp[i+j] %= mod

    print(dp[K])


if __name__ == '__main__':
    main()
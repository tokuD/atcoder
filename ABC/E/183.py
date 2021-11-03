# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
import heapq
# sys.setrecursionlimit(10**5)

def main():
    mod = 10**9 + 7
    H,W = map(int, input().split())
    G = [list(input().rstrip()) for _ in range(H)]
    dp = [[0]*W for _ in range(H)]
    X = [[0]*W for _ in range(H)]
    Y = [[0]*W for _ in range(H)]
    Z = [[0]*W for _ in range(H)]
    dp[0][0] = 1

    for h in range(H):
        for w in range(W):
            if G[h][w] == '#': continue
            if h == w == 0: continue
            if w-1 >= 0:
                X[h][w] = X[h][w-1] + dp[h][w-1]
                X[h][w] %= mod
            if h-1 >= 0:
                Y[h][w] = Y[h-1][w] + dp[h-1][w]
                Y[h][w] %= mod
            if h-1 >= 0 and w-1 >= 0:
                Z[h][w] = Z[h-1][w-1] + dp[h-1][w-1]
                Z[h][w] %= mod
            dp[h][w] = X[h][w] + Y[h][w] + Z[h][w]
            dp[h][w] %= mod

    print(dp[H-1][W-1])




if __name__ == '__main__':
    main()
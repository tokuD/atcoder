# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def calc(X:List[str], Y:List[str])->int:
    dp = [[0]*(len(X)) for _ in range(len(Y))]

    for y in range(1,len(Y)):
        for x in range(1,len(X)):
            if X[x] == Y[y]:
                dp[y][x] = max(dp[y][x], dp[y-1][x-1]+1)
            else:
                dp[y][x] = max(dp[y][x], dp[y][x-1], dp[y-1][x])

    return dp[-1][-1]

def main():
    ans = []
    q = int(input())
    for _ in range(q):
        X = ['.'] + list(input().rstrip())
        Y = ['.'] + list(input().rstrip())
        ans.append(calc(X,Y))

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
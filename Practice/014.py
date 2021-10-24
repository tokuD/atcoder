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
    N,K = map(int, input().split())
    A = list(map(int, input().split()))

    INF = 10**20
    ans = INF

    for bit in range(2**(N-1)):
        now = A[0]
        cost = 0
        heights = [A[0]]
        for i in range(N-1):
            if bit >> i & 1:
                cost += max(0, now+1 - A[i+1])
                now = max(now+1, A[i+1])
                heights.append(now)
            else:
                heights.append(A[i+1])
        count = 0
        mi = 0
        for i in range(N):
            if mi < heights[i]:
                mi = heights[i]
                count += 1
        if count >= K:
            ans = min(ans, cost)

    print(ans)


if __name__ == '__main__':
    main()
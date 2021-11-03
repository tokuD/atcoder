# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N,K = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(N)]

    A = range(1,N)
    ans = 0
    for per in permutations(A):
        s = 0
        total = 0
        for g in per:
            total += G[s][g]
            s = g
        total += G[s][0]
        if total == K:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
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
    H,W = map(int, input().split())
    total = 0
    INF = 10**10
    mi = INF
    for i in range(H):
        A = list(map(int, input().split()))
        mi = min(mi,min(A))
        total += sum(A)
    print(total-mi*H*W)


if __name__ == '__main__':
    main()
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
    N,X = map(int, input().split())
    S = list(input().rstrip())
    for s in S:
        if s == 'o':
            X += 1
        else:
            X = max(0,X-1)

    print(X)


if __name__ == '__main__':
    main()
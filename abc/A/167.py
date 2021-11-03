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
    S = list(input().rstrip())
    T = list(input().rstrip())
    if S == T[:-1]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
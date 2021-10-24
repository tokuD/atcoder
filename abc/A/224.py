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
    if S[-2:] == ['e','r']:
        print('er')
    else:
        print('ist')


if __name__ == '__main__':
    main()
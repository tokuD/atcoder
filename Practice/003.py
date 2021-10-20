#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    S = list(input()) + ['W']
    target = ['A','C','G','T']
    ans = 0
    now = 0
    for s in S:
        if s in target:
            now += 1
        else:
            ans = max(ans,now)
            now = 0

    print(ans)

if __name__ == '__main__':
    main()
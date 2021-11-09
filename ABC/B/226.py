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
    N = int(input())
    L = set()
    for _ in range(N):
        l = input().rstrip()
        L.add(l)

    print(len(L))


if __name__ == '__main__':
    main()
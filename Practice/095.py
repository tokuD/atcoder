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
    A,B,K = map(int,input().split())
    Takahashi = A
    Aoki = B
    if Takahashi >= K:
        Takahashi -= K
    else:
        rest = K - Takahashi
        Takahashi = 0
        Aoki -= rest
        Aoki = max(Aoki, 0)

    print(Takahashi, Aoki)

if __name__ == '__main__':
    main()
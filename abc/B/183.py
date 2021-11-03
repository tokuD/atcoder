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
    sx,sy,gx,gy = map(int, input().split())
    print(sx-sy*(sx-gx)/(sy+gy))


if __name__ == '__main__':
    main()
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
    x0,y0 = map(int, input().split())
    x1,y1 = map(int, input().split())
    if (x0,y0) == (x1,y1):
        print(0)
        exit()
    if (x0+y0 == x1+y1) or (x0-y0 == x1-y1) or (abs(x0-x1)+abs(y0-y1) <= 3):
        print(1)
        exit()
    if abs(x0-x1)+abs(y0-y1) <= 6:
        print(2)
        exit()
    dy = y1-y0
    dx = abs(x1-x0) - abs(dy)
    if dx % 2 == 0:
        print(2)
    else:
        if abs(dx) <= 3:
            print(2)
        else:
            print(3)

if __name__ == '__main__':
    main()
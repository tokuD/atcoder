# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)
from math import sqrt

def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 0
    count = 0

    for per in permutations(range(N)):
        n = len(per)
        count += 1
        for i in range(1,n):
            x0,y0 = XY[per[i-1]]
            x1,y1 = XY[per[i]]
            ans += sqrt((x0-x1)**2 + (y0-y1)**2)

    print(ans/count)


if __name__ == '__main__':
    main()
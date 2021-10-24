# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 0
    for xy in combinations(XY, 3):
        x0,y0 = xy[0]
        x1,y1 = xy[1]
        x2,y2 = xy[2]
        if x0 == x1 and x0 == x2:
            continue
        if x0 == x1 or x0 == x2 or x1 == x2:
            ans += 1
            continue
        a = (y0-y1)/(x0-x1)
        b = (y0-y2)/(x0-x2)
        c = (y1-y2)/(x1-x2)
        if a == b and a == c:
            continue
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
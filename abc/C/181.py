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
    xy = []
    for _ in range(N):
        x,y = map(int, input().split())
        xy.append((x,y))

    ans = 'No'

    for a,b,c in combinations(xy, 3):
        x0,y0 = a
        x1,y1 = b
        x2,y2 = c
        if (x2-x0)*(y1-y0) == (x1-x0)*(y2-y0):
            ans = 'Yes'

    print(ans)


if __name__ == '__main__':
    main()
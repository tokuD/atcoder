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
    m = int(input())
    tmp = [tuple(map(int,input().split())) for _ in range(m)]
    dx0,dy0 = -tmp[0][0], -tmp[0][1]
    starts = set()
    for i,j in tmp:
        x,y = i+dx0, j+dy0
        starts.add((x,y))
    n = int(input())
    pic = [tuple(map(int,input().split())) for _ in range(n)]

    for dx1,dy1 in pic:
        dx1 *= -1
        dy1 *= -1
        count = 0
        for x,y in pic:
            x,y = x+dx1, y+dy1
            if (x,y) in starts:
                count += 1
            if count == m:
                print(dx0-dx1, dy0-dy1)
                exit()


if __name__ == '__main__':
    main()
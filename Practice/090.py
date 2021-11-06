#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from math import sqrt
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N,M = map(int,input().split())
    C = [tuple(map(int,input().split())) for _ in range(N)]
    D = [tuple(map(int,input().split())) for _ in range(M)]

    if M == 0:
        tmp = 200
        for c in C:
            tmp = min(tmp, c[2])
        print(tmp)
        exit()

    ok = 0
    ng = 200
    while abs(ok-ng) > 10**(-7):
        flag = True
        r0 = (ok+ng)/2
        for i in range(M):
            x0,y0 = D[i]
            for j in range(N):
                x1,y1,r1 = C[j]
                if (r0+r1)**2 > (x1-x0)**2+(y1-y0)**2:
                    flag = False
            for j in range(i+1,M):
                x1,y1 = D[j]
                if (r0+r0)**2 > (x1-x0)**2+(y1-y0)**2:
                    flag = False
        if flag:
            ok = r0
        else:
            ng = r0

    print(ok)

if __name__ == '__main__':
    main()
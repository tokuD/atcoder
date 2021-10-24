# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def f(t:float, P:float):
    return t + P * pow(2, -(2*t/3))

def main():
    P = float(input())
    l = 0
    r = 10 ** 19
    while abs(f(l,P) - f(r,P)) > pow(10,-9):
        c1 = (l*2+r) / 3
        c2 = (l+r*2) / 3
        if f(c1,P) >= f(c2,P):
            l = c1
        else:
            r = c2

    print(f(l,P))


if __name__ == '__main__':
    main()
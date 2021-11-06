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

    ans = []

    while True:
        n = int(input())
        if n == 0: break
        t = [0]*(10**5)
        for _ in range(n):
            S,G = list(input().split())
            s = S.split(':')
            g = G.split(':')
            t0 = int(s[0])*(60**2) + int(s[1])*60 + int(s[2])
            t1 = int(g[0])*(60**2) + int(g[1])*60 + int(g[2])
            t[t0] += 1
            t[t1] -= 1
        for i in range(1,10**5):
            t[i] += t[i-1]
        ans.append(max(t))

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
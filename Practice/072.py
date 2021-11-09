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
    mod = 10**9+7
    W,H = map(int,input().split())
    ans = 1
    A,M,N = 1,1,1
    for i in range(2,H+W-1):
        A *= i
        A %= mod
        if i <= H-1:
            M *= i
            M %= mod
        if i <= W-1:
            N *= i
            N %= mod

    ans = A
    ans *= pow(M,mod-2,mod)
    ans %= mod
    ans *= pow(N,mod-2,mod)
    ans %= mod

    print(ans)

if __name__ == '__main__':
    main()
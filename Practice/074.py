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
    n = int(input())
    k = int(input())
    A,B,C = 1,1,1

    for i in range(2,n+k):
        A *= i
        A %= mod
        if i<=k:
            B *= i
            B %= mod
        if i<=(n-1):
            C *= i
            C %= mod

    ans = A
    ans *= pow(B,mod-2,mod)
    ans %= mod
    ans *= pow(C,mod-2,mod)
    ans %= mod

    print(ans)

if __name__ == '__main__':
    main()
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
    X,Y = map(int,input().split())
    ans = 0
    if (2*X-Y) % 3 != 0 or (2*Y-X) % 3 != 0:
        print(ans)
        exit()

    a = (2*X-Y)//3
    b = (2*Y-X)//3

    if a < 0 or b < 0:
        print(0)
        exit()

    ans = 1
    A,M,N = 1,1,1
    for i in range(2,a+b+1):
        A *= i
        A %= mod
        if i<=a:
            M *= i
            M %= mod
        if i<=b:
            N *= i
            N %= mod

    ans *= A
    ans *= pow(M,mod-2,mod)
    ans %= mod
    ans *= pow(N,mod-2,mod)
    ans %= mod

    print(ans)

if __name__ == '__main__':
    main()
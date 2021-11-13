# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def half(X:int, Y:int, B:int):
    ok = 0
    ng = 10**19
    while abs(ok-ng)>1:
        n = (ok+ng)//2
        if X+n*B<Y:
            ok = n
        else:
            ng = n
    return ok

def main():
    X,Y,A,B = map(int, input().split())

    ans = 0
    now = 0
    while True:
        ans = max(ans, now+half(X,Y,B))
        X *= A
        if X >= Y: break
        now += 1

    print(ans)

if __name__ == '__main__':
    main()
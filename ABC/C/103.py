# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def f(m:int,A:List[int]):
    res = 0
    for a in A:
        res += m % a
    return res

def main():
    N = int(input())
    A = list(map(int, input().split()))

    m = 1
    for a in A:
        m *= a
    ans = f(m-1,A)
    print(ans)

if __name__ == '__main__':
    main()
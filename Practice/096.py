#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def tousa_sum(a:int,d:int,n:int)->int:
    """
    等差数列の和を返す
    a:初項、d:公差、n:項数
    """
    return n*(2*a+(n-1)*d)//2

def main():
    N = int(input())
    if N == 1:
        print(0)
        exit()
    if N == 2:
        print(1)
        exit()

    ans = 1
    ans += tousa_sum(2,1,N-2)

    print(ans)


if __name__ == '__main__':
    main()
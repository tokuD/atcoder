#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)
from math import sqrt


def main():
    N = int(input())
    ans = 0

    for n in range(1,N+1,2):
        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count += 1
        if count == 8:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
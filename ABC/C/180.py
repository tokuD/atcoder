# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
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
    ans = []
    for i in range(1,int(sqrt(N))+1):
        if N % i == 0:
            ans.append(i)
            if i != N//i:
                ans.append(N//i)

    ans.sort()
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
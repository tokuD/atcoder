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
    X = list(map(lambda x:abs(int(x)), input().split()))
    a = sum(X)
    b = 0
    c = max(X)
    for x in X:
        b += pow(x,2)

    print(a)
    print(sqrt(b))
    print(c)


if __name__ == '__main__':
    main()
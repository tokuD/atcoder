# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    a = 0
    b = 0

    for i,seq in enumerate(permutations(range(1,N+1))):
        if list(seq) == P:
            a = i+1
        if list(seq) == Q:
            b = i+1

    print(abs(a-b))

if __name__ == '__main__':
    main()
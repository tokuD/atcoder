# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N = list(input().rstrip())
    A = list(map(int, N))
    k = len(A)

    for i in range(k): #* 消す個数
        for c in combinations(A,k-i):
            if sum(c) % 3 == 0:
                print(i)
                exit()

    print(-1)

if __name__ == '__main__':
    main()
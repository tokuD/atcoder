# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    count = 0
    for i in range(2,1001):
        res = 0
        for a in A:
            if a % i == 0: res += 1
        if count <= res:
            count = res
            ans = i

    print(ans)

if __name__ == '__main__':
    main()
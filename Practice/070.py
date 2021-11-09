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
    mod = 10**9+7
    m,n = map(int, input().split())
    ans = pow(m,n,mod)
    print(ans)


if __name__ == '__main__':
    main()
# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from math import factorial
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    L = int(input())
    n = L-1
    ans = factorial(n) // (factorial(n-11)*factorial(11))
    print(ans)




if __name__ == '__main__':
    main()
# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N = int(input())
    ans = 0

    for i in range(1,N+1):
        if '7' in list(str(i)):
            continue
        if '7' in list(oct(i)):
            continue
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    R,C = map(int,input().split())
    mochi = [list(map(int,input().split())) for _ in range(R)]

    ans = 0

    for bit in range(2**R):
        res = 0
        for i in range(C):
            count = 0
            for j in range(R):
                a = mochi[j][i]
                if bit >> j & 1:
                    a = a ^ 1
                count += a
            res += max(count, R-count)
        ans = max(ans,res)

    print(ans)



if __name__ == '__main__':
    main()
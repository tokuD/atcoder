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
    N = int(input())
    S = list(input())
    ans = 0

    for i in range(10):
        for j in range(10):
            for k in range(10):
                count = 0
                target = [str(i), str(j), str(k)]
                for s in S:
                    if s == target[count]:
                        count += 1
                    if count == 3:
                        ans += 1
                        break

    print(ans)

if __name__ == '__main__':
    main()
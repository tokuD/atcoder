#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    ans = []

    while True:
        res = 0
        n,x = map(int,input().split())
        if n == 0 and x == 0:
            break
        for i,j,k in combinations(range(1,n+1),3):
            if i + j + k == x:
                res += 1
        ans.append(res)


    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
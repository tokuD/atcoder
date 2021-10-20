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
    AB = []
    target = set()
    for _ in range(N):
        a,b = map(int,input().split())
        AB.append((a,b))
        target.add(a)
        target.add(b)

    INF = 10**20
    ans = INF

    for s in target:
        for g in target:
            if g < s:
                continue
            res = 0
            for a,b in AB:
                if s <= a and b <= g:
                    res += g-s
                elif a < s and g < b:
                    res += 2*(b-a) - (g-s)
                elif g < b:
                    res += 2*b -s -g
                else:
                    res += s + g - 2*a
            ans = min(ans,res)

    print(ans)


if __name__ == '__main__':
    main()
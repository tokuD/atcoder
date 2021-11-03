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
    child = [set() for _ in range(N)]
    for _ in range(N-1):
        a,b = map(lambda x:int(x)-1, input().split())
        child[a].add(b)
        child[b].add(a)
    ans = 'No'

    for a in child:
        if len(a) == N-1:
            ans = 'Yes'

    print(ans)

if __name__ == '__main__':
    main()
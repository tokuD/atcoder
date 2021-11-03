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
    n = int(input())
    cnt = [0]*(10**6+2)
    for _ in range(n):
        a,b = map(int, input().split())
        cnt[a] += 1
        cnt[b+1] -= 1
    for i in range(1,10**6+1):
        cnt[i] += cnt[i-1]

    print(max(cnt))


if __name__ == '__main__':
    main()
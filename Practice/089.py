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
    A = list(map(int,input().split()))
    A.append(A[-1])
    cnt = []
    length = 0
    last = 2
    for i in range(N+1):
        if last != A[i]:
            length += 1
        else:
            cnt.append(length)
            length = 1
        last = A[i]

    ans = 0
    for i in range(len(cnt)-2):
        ans = max(ans, cnt[i]+cnt[i+1]+cnt[i+2])

    if len(cnt) < 3:
        ans = sum(cnt)

    print(ans)


if __name__ == '__main__':
    main()
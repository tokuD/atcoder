# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = defaultdict(int)
    length = 0
    kind = 0
    ans = 0
    for i in range(N):
        a = A[i]
        if cnt[a] == 0:
            kind += 1
        length += 1
        cnt[a] += 1
        while kind > K:
            rm = A[i-length+1]
            length -= 1
            cnt[rm] -= 1
            if cnt[rm] == 0:
                kind -= 1
        ans = max(ans,length)

    print(ans)

if __name__ == '__main__':
    main()
# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0]*N
    cnt[0] = A[0]
    for i in range(1,N):
        cnt[i] = cnt[i-1] + A[i]

    ma = [0]*N
    ma[0] = max(0,cnt[0])
    for i in range(1,N):
        ma[i] = max(ma[i-1], cnt[i])

    ans = 0
    now = 0
    for i in range(N):
        ans = max(ans,now+ma[i])
        # print(now,ma[i])
        now += cnt[i]

    print(ans)

if __name__ == '__main__':
    main()
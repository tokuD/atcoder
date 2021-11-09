#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
from itertools import permutations,combinations,accumulate
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    mod = 10**9+7
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    C = [0] + list(map(lambda x:int(x)-1,input().split())) + [0]
    ans = 0
    cnt = [0]*N #* 街0から街iまでの距離
    for i in range(1,N):
        # cnt[i] = cnt[i-1] % mod + pow(A[i-1],A[i],mod)
        # cnt[i] %= mod
        # cnt[i] %= mod
        cnt[i] = pow(A[i-1],A[i],mod)

    # cnt = list(accumulate(cnt))
    for i in range(1,N):
        cnt[i] += cnt[i-1]
        # cnt[i] %= mod

    for i in range(Q+1):
        s = C[i]
        g = C[i+1]
        ans += abs(cnt[s]-cnt[g])
        ans %= mod

    print(ans)

if __name__ == '__main__':
    main()
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
    N,M = map(int, input().split())
    P = list(map(int, input().split()))
    A = [0] #* A[i]:鉄道iの切符の運賃
    B = [0]
    C = [0]
    for _ in range(N-1):
        a,b,c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    cnt = [0]*(N+1)
    for i in range(1,M):
        s,g = P[i-1],P[i]
        s,g = min(s,g),max(s,g)
        cnt[s] += 1
        cnt[g] -= 1
    for i in range(1,N+1):
        cnt[i] += cnt[i-1]
    ans = 0
    for i in range(1,N):
        x = cnt[i]
        ans += min(A[i]*x, C[i]+B[i]*x)

    print(ans)

if __name__ == '__main__':
    main()
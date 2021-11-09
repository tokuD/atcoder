# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

# def dfs(n:int,T: List[int], K:List[int], A:List[List[int]], learned:List[bool],ans:int):
#     if learned[n]: return
#     for a in A[n]:
#         if learned[a]: continue
#         dfs(a,T,K,A,learned,ans)
#     learned[n] = True
#     ans += K[n]

def main():
    N = int(input())
    T = []
    # K = []
    A = []
    learned = [False]*N
    for _ in range(N):
        l = list(map(lambda x:int(x)-1, input().split()))
        t = l[0]+1
        # k = l[1]
        a = l[2:]
        T.append(t)
        # K.append(k)
        A.append(a)

    # dfs(N-1,T,K,A,learned,ans)
    # print(ans)
    ans = 0
    Q = deque()
    Q.append(N-1)
    while len(Q)>0:
        x = Q.popleft()
        if learned[x]: continue
        learned[x] = True
        ans += T[x]
        # print(T[x])
        for chi in A[x]:
            if learned[chi]: continue
            Q.append(chi)

    print(ans)



if __name__ == '__main__':
    main()
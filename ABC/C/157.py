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
    N,M = map(int, input().split())
    ans = ['0']*N
    for _ in range(M):
        s,c = map(int, input().split())
        if ans[s-1] == '0' or ans[s-1] == str(c):
            ans[s-1] = str(c)
        else:
            print(-1)
            exit()
        if N != 1 and s == 1 and c == 0:
            print(-1)
            exit()
    if N > 1 and ans[0] == '0':
        ans[0] = '1'

    print(''.join(ans))

    # S = []
    # C = []
    # for _ in range(M):
    #     s,c = map(int, input().split())
    #     S.append(s)
    #     C.append(c)

    # for i in range(1000):
    #     ok = True
    #     n = list(str(i))
    #     if len(n) != N: continue
    #     for s,c in zip(S,C):
    #         if n[s-1] != str(c):
    #             ok = False
    #             break
    #     if ok:
    #         print(i)
    #         exit()

    # print(-1)

if __name__ == '__main__':
    main()
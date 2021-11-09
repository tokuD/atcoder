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
    S = list(input().rstrip())
    T = list(input().rstrip())

    ans = []

    dp = [[False]*len(S) for _ in range(len(T))]

    for i in range(len(T)):
        for j in range(len(S)):
            if i == 0:
                if T[i] == S[j] or S[j] == '?': dp[i][j] = True
            if dp[i][j]:
                if i+1<len(T) and j+1<len(S):
                    if T[i+1] == S[j+1] or S[j+1] == '?':
                        dp[i+1][j+1] = True

    for i in range(len(dp[-1])):
        if dp[-1][i]:
            res = S[:i-len(T)+1] + T + S[i+1:]
            res = list(map(lambda x:'a' if x=='?' else x, res))
            ans.append(''.join(res))

    # print(dp[-1])
    if len(ans) == 0:
        print('UNRESTORABLE')
    else:
        ans.sort()
        print(ans[0])

if __name__ == '__main__':
    main()
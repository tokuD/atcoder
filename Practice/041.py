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
    D,N = map(int, input().split())
    T = [0] + [int(input()) for _ in range(D)] #* T[i]:i日目の気温
    A = [0] #* A[i]:服iの最低気温
    B = [0] #* B[i]:服iの最高気温
    C = [0] #* C[i]:服iの派手さ
    for _ in range(N):
        a,b,c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    c_max = max(C)
    INF = 10**20
    dp = [[-INF]*(c_max+1) for _ in range(D+1)] #* dp[i][j]:i日目に派手さjの服を着る時の、それまでの合計ポイント

    for i in range(1,D+1): #* i日目
        for j in range(1,N+1): #* j番目の服
            a,b,c,t = A[j],B[j],C[j],T[i]
            if not (a<=t<=b): continue
            if i == 1:
                dp[i][c] = 0
                continue
            for k in range(c_max+1): #* 前日の服の派手さk
                dp[i][c] = max(dp[i][c], dp[i-1][k] + abs(c-k))

    ans = 0
    for i in range(c_max+1):
        ans = max(ans, dp[-1][i])

    print(ans)

if __name__ == '__main__':
    main()
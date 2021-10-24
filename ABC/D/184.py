# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    A,B,C = map(int, input().split())

    #* dp[i][j][k]:状態(i,j,k)となる確率
    dp = [[[0]*(101) for i in range(101)] for j in range(101)]
    dp[A][B][C] = 1
    #* bfs的にシミュレーション
    Q = deque()
    Q.append((A,B,C))
    while len(Q) > 0:
        a,b,c = Q.popleft()
        if a == 100 or b == 100 or c == 100:
            continue

        p = dp[a][b][c]

        #* aを増やす場合
        if a > 0:
            dp[a+1][b][c] += p * a / (a+b+c)
            Q.append((a+1,b,c))

        #* bを増やす場合
        if b > 0:
            dp[a][b+1][c] += p * b / (a+b+c)
            Q.append((a,b+1,c))

        #* cを増やす場合
        if c > 0:
            dp[a][b][c+1] += p * c / (a+b+c)
            Q.append((a,b,c+1))

    ans = 0

    #* cが100枚になって終了した場合
    for i in range(A,101):
        for j in range(B,101):
            n = (i-A) + (j-B) + (100-C)
            ans += n * dp[i][j][100]

    #* bが100枚
    for i in range(A,101):
        for k in range(C,101):
            n = (i-A) + (100-B) + (k-C)
            ans += n * dp[i][100][k]

    #* aが100枚
    for j in range(B,101):
        for k in range(C,101):
            n = (100-A) + (j-B) + (k-C)
            ans += n * dp[100][j][k]

    print(ans)

if __name__ == '__main__':
    main()
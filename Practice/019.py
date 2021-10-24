# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    d = int(input()) #* 環状線の全長
    n = int(input()) #* 店舗の個数
    m = int(input()) #* 注文の個数
    D = [0] + [int(input()) for _ in range(n-1)] + [d] #* 店舗の位置
    K = [int(input()) for _ in range(m)] #* 宅配先の場所

    D.sort()

    ans = 0
    for k in K:
        l = bisect_left(D, k)
        ans += min(abs(D[l]-k), abs(D[l-1]-k))

    print(ans)

if __name__ == '__main__':
    main()
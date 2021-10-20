#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    A,B,C,X,Y = map(int,input().split())
    INF = 10**20
    ans = INF

    for i in range(0,2*max(X,Y)+1, 2):
        x = max(0, X - i//2)
        y = max(0, Y - i//2)
        price = A * x + B * y + C * i
        ans = min(ans,price)

    print(ans)

if __name__ == '__main__':
    main()
# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def gcd(x:int,y:int):
    if y == 0: return x
    return gcd(y,x%y)

def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x,y = map(int, input().split())
        X.append(x)
        Y.append(y)

    magic = set()

    for i,j in permutations(range(N),2):
        dx = X[j]-X[i]
        dy = Y[j]-Y[i]
        # print(dx,dy)
        k = gcd(abs(dx),abs(dy))
        dx //= k
        dy //= k
        magic.add(str(dx)+':'+str(dy))

    print(len(magic))
    # print(magic)



if __name__ == '__main__':
    main()
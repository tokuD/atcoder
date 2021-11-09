# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
from math import sqrt
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    n = int(input())
    ans = [str(n)+':']
    for i in range(2,int(sqrt(n))+1):
        while n % i == 0:
            n //= i
            ans.append(str(i))
    if n != 1:
        ans.append(str(n))

    print(' '.join(ans))

if __name__ == '__main__':
    main()
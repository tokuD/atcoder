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
    X = list(input())
    ans = []
    res = 0
    for i in range(len(X)):
        if X[i] == '.':
            a = X[i+1]
            if int(a) >= 5:
                res += 1
            break
        ans.append(X[i])

    a = int(''.join(ans))
    print(a+res)

if __name__ == '__main__':
    main()
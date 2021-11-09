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
    C = [list(map(int, input().split())) for _ in range(3)]
    ans = 'No'
    for a1 in range(101):
        for a2 in range(101):
            for a3 in range(101):
                flag = True
                for j in range(3):
                    if not (C[0][j]-a1 == C[1][j]-a2 == C[2][j]-a3):
                        flag = False
                if flag:
                    ans = "Yes"

    print(ans)


if __name__ == '__main__':
    main()
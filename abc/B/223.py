# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    S = list(input().rstrip())
    S = deque(S)
    ans = []
    A = S.copy()
    for i in range(len(S)):
        a = A.popleft()
        A.append(a)
        ans.append(''.join(A))
    A = S.copy()
    for i in range(len(S)):
        a = A.pop()
        A.appendleft(a)
        ans.append(''.join(A))
    ans.sort()
    
    # print(ans)
    print(ans[0])
    print(ans[-1])


if __name__ == '__main__':
    main()
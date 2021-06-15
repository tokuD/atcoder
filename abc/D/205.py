import numpy as np

N,Q = map(int,input().split())
a = [0] * (10**18)
for n in N:
    c = int(input())
    a[c-1] = 1

ans = np.array([1] * (10**18))

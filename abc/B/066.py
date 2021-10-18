from collections import deque
S = list(input())

while True:
    S.pop()
    S.pop()
    n = len(S)
    mid = n // 2
    l = S[:mid]
    r = S[mid:]
    if l == r:
        print(n)
        break

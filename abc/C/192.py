import sys
sys.setrecursionlimit(10**6)
N,K = map(int,input().split())

def g1(x: int):
    x = list(str(x))
    x.sort(reverse=True)
    return int(''.join(x))

def g2(x: int):
    x = list(str(x))
    x.sort()
    return int(''.join(x))

def f(x: int):
    return g1(x) - g2(x)

def a(n: int):
    return N if n == 0 else f(a(n-1))

print(a(K))
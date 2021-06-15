A,B,C = map(int,input().split())

def gcd(a,b):
    return b if a % b == 0 else gcd(b, a % b)

s = gcd(A, gcd(B,C))

print(int(A//s + B//s + C//s - 3))

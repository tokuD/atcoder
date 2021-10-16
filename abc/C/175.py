X,K,D = map(int, input().split())

n = abs(X) // D
X = abs(X)
if K <= n:
    print(abs(X-K*D))
elif (K-n) % 2 == 0:
    print(abs(X-n*D))
else:
    print(abs(X-(n+1)*D))

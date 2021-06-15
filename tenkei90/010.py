N = int(input())

one = [0] #!1組のSi
two = [0] #!2組のSi
ansers = []
a = 0
b = 0
for i in range(N):
    c,p = map(int,input().split())
    if c == 1:
        a += p
    else:
        b += p
    one.append(a)
    two.append(b)

Q = int(input())
for j in range(Q):
    l,r = map(int,input().split())
    a = str(one[r]-one[l-1])
    b = str(two[r]-two[l-1])
    ansers.append((a,b))
# print(one)
# print(two)
for ans in ansers:
    print(ans[0],ans[1],sep=' ')
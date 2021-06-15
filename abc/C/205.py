a,b,c = map(int,input().split())
ans = ''

if c % 2 == 0:
    c = 2
else:
    c = 1

r = a ** c
l = b ** c

if r == l:
    ans = '='
elif r > l:
    ans = '>'
elif r < l:
    ans = '<'

print(ans)

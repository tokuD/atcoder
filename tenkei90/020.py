a,b,c = map(int,input().split())

ans = ''

if a < c**b:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)

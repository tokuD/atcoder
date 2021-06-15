a,b = map(str, input().split())
num = int(a+b)
# print(num)
ans = 'No'

for i in range(1,1001):
    if i**2 == num:
        ans = 'Yes'
    if i**2 > num:
        break

print(ans)

N = int(input())
A = list(map(int,input().split()))
count = 0
A.sort()
ac = []
for a in A:
    if a in ac:
        flag = False
        print('No')
        exit()
    ac.append(a)
ans = 'No'
if ac[-1] <= N:
    ans = 'Yes'

print(ans)

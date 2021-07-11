N = int(input())
name = {}
ans = []
for i in range(1,N+1):
    s = input()
    try:
        if name[s] == 1:
            continue
    except KeyError:
        name[s] = 1
        ans.append(i)

for i in ans:
    print(i)

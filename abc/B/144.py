N = int(input())

ans = 'No'
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == N:
            ans = 'Yes'
            break
        else:
            continue
print(ans)

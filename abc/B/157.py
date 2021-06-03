A = []
for i in range(3):
    row = list(map(int, input().split()))
    for j in range(3):
        A.append(row[j])

N = int(input())
b = [int(input()) for _ in range(N)]
x = [0 for _ in range(3)]
y = [0 for _ in range(3)]
z1 = 0
z2 = 0
for num in b:
    for j,a in enumerate(A):
        if a == num:
            if j+1 in [1,2,3]:
                x[0] += 1
            if j+1 in [4,5,6]:
                x[1] += 1
            if j+1 in [7,8,9]:
                x[2] += 1
            if j+1 in [1,4,7]:
                y[0] += 1
            if j+1 in [2,5,8]:
                y[1] += 1
            if j+1 in [3,6,9]:
                y[2] += 1
            if j+1 in [1,5,9]:
                z1 += 1
            if j+1 in [3,5,7]:
                z2 += 1

ans = 'No'

if (z1 == 3) or (z2 == 3) or (3 in x) or (3 in y):
    ans = 'Yes'

print(ans)

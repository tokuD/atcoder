N = int(input())
x = []
y = []
xy = []
ans_list = []
for i in range(N):
    a, b = map(int, input().split())
    x.append([i, a])
    y.append([i, b])
    xy.append([i, a, b])

# print(x)
# print(y)

x_sorted = sorted(x, reverse=True, key=lambda x:x[1])
y_sorted = sorted(y, reverse=True, key=lambda x:x[1])


x_cut = [*x_sorted[:2], *x_sorted[-2:]]
y_cut = [*y_sorted[:2], *y_sorted[-2:]]
# print(x_cut, y_cut)

x_cut = [house for house, zahyou in x_cut]
y_cut = [house for house, zahyou in y_cut]

# print(x_cut, y_cut)

for pair in xy:
    if pair[0] in x_cut:
        ans_list.append([pair[1], pair[2]])
    else:
        if pair[0] in y_cut:
            ans_list.append([pair[1], pair[2]])
    continue

ans = []

for i in range(len(ans_list)):
    for j in range(i+1, len(ans_list)):
        kouho = max(abs(ans_list[i][0]-ans_list[j][0]), abs(ans_list[i][1]-ans_list[j][1]))
        ans.append(kouho)

ans.sort(reverse=True)

print(ans[1])

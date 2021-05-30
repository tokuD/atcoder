S = input()
ans = []
def judge(s):
    return int(s in ['A', 'C', 'G', 'T'])


for s in S:
    ans.append(judge(s))

m = 0

for i in range(len(ans)):
    if ans[i] == 0:
        continue
    total = 1
    for j in range(i+1, len(ans)):
        if ans[j] == 0:
            break
        else:
            total += 1
            continue
    if total >= m:
        m = total

print(m)

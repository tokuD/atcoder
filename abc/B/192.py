S = list(input())
ans = True
for i in range(len(S)):
    if (i+1) % 2 == 0:
        if S[i] != S[i].upper():
            ans = False
    else:
        if S[i] != S[i].lower():
            ans = False

if ans:
    print('Yes')
else:
    print('No')
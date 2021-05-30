s = list(input())
ans = "NO"
while len(s) >= 5:
    if s[:7] == list("dreamer") and s[7:10] != list("ase"):
        del s[:7]
    elif s[:6] == list("eraser"):
        del s[:6]
    elif s[:5] == list("dream"):
        del s[:5]
    elif s[:5] == list("erase"):
        del s[:5]
    else:
        break

if len(s) == 0:
    ans = "YES"

print(ans)

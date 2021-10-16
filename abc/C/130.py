W,H,x,y = map(int, input().split())

ans = [W*H//2]
if W//2 == x and H//2 == y:
    ans.append(1)
else:
    ans.append(0)

print(ans[0],ans[1])
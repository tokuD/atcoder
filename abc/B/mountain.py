N = int(input())

mountains = {}

for _ in range(N):
    # row = input().split(" ")
    # name = row[0]
    # height = int(row[1])
    name, height = input().split()
    mountains[name] = int(height)

mountains = sorted(mountains.items(), key=lambda x:x[1], reverse=True)

ans = mountains.pop(1)

# print(mountains)

print(ans[0])
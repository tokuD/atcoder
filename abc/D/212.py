Q = int(input())
bag = []
plus = []
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        bag.append(query[1])
    elif query[0] == 2:
        plus.append()
    else:

N = int(input())
S = [input() for _ in range(N)]
vote = {}
vote_list = []
for i in range(N):
    try:
        vote[S[i]] += 1
    except KeyError:
        vote[S[i]] = 1
count = ['',0]
for name,value in vote.items():
    if count[1] < value:
        count = [name,value]

print(count[0])

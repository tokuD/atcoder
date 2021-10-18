from collections import defaultdict
N = int(input())
dic = {}

for _ in range(N):
    s = input()
    dic[s] = 1

for key,value in dic.items():
    a = '!' + key
    try:
        if dic[a] == 1:
            print(key)
            exit()
    except KeyError:
        continue

print('satisfiable')
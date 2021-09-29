from collections import Counter
list_ = []
num_list = []
for i in range(1000):
    if i % 8 == 0:
        num_list.append(i)
        s = list(map(int,str(i)))
        if not 0 in s and len(s) == 3:
            list_.append(s)

S = input()
if len(S) < 3:
    S1 = int(S)
    S2 = int(S[::-1])
    if S1 in num_list or S2 in num_list:
        print('Yes')
        exit()

S = list(map(int,str(S)))


s_counter = [0 for _ in range(10)] #*入力Sに何が何個あるか

for i in range(len(S)):
    n = S[i]
    s_counter[n] += 1

for i in range(len(list_)):
    a = s_counter.copy()
    x,y,z = list_[i]
    a[x] -= 1
    a[y] -= 1
    a[z] -= 1
    if (a[x] >= 0) and (a[y] >= 0) and (a[z] >= 0):
        print('Yes')
        exit()
print('No')

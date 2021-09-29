S = [input() for _ in range(3)]
T = list(map(int,list(input())))

for i in range(len(T)):
    a = T[i] -1
    if i == len(T)-1:
        print(S[a])
    else:
        print(S[a],end='')
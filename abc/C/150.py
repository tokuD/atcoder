from itertools import permutations

N = int(input())
P = input().split()
Q = input().split()
P = int("".join(P))
Q = int("".join(Q))

numbers = [str(i) for i in range(1,N+1)]
order = []
for number in permutations(numbers):
    number = int(''.join(number))
    order.append(number)

order.sort()
# print(order)
a = 0
b = 0

for i,num in enumerate(order):
    if P == num:
        a = i+1
    if Q == num:
        b = i+1

print(abs(a-b))

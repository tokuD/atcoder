A,B,W = map(float, input().split())
W *= 1000
INF = 1e10
mi = INF
ma = 0

# N = int(W // A)
# for i in range(N+1)[::-1]:
#     amari = W - A * i
#     j = int(amari // A)
#     find = False
#     while amari <= B * j:
#         if A * j <= amari:
#             ma = i + j
#             find = True

#             break
#         j -= 1
#     if find:
#         break

# N = int(W // B)
# for i in range(N+1)[::-1]:
#     amari = W - B * i
#     j = int(amari // B)
#     find = False
#     while A * j <= amari:
#         if amari <= B * j:
#             mi = i + j
#             find = True
#             break
#         j += 1
#     if find:
#         break

for i in range(1,10**6+1):
    if A * i <= W <= B * i:
        mi = min(mi,i)
        ma = max(ma,i)

if mi == INF and ma == 0:
    print('UNSATISFIABLE')
else:
    print(mi,ma)

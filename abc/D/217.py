L,Q = map(int,input().split())
CX = [list(map(int,input().split())) for _ in range(Q)]
wood = [0,L] #*切れ端の先端をメモ
dic = {0:0,L:L}
def half_search(x,sorted_list):
    n = len(sorted_list)
    half = n // 2
    left = sorted_list[:half]
    right = sorted_list[half:]
    if left[-1] < x < right[0]:
        return right[0] - left[-1]
    if x < left[-1]:
        return half_search(x,left)
    if right[0] < x:
        return half_search(x,right)



for i in range(Q):
    c,x = CX[i]
    if c == 1:
        #* woodの間に挿入
        wood.append(x)
        dic[x] = x
    else:
        print(half_search(x,wood))

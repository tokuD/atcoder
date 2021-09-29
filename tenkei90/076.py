def half_search(R,Sum):
    n = len(Sum)
    center = n // 2
    if n>1:
        l = Sum[:center]
        r = Sum[center:]
        if R <= l[-1]:
            return half_search(R,l)
        else:
            return half_search(R,r)
    else:
        return Sum[0] == R

def main():
    N = int(input())
    A = list(map(int,input().split()))
    total = sum(A)
    Sum = [A[0]]
    ans = 'No'
    for i in range(1,2*N):
        j = i
        if i >= N:
            j -= N
        Sum.append(Sum[i-1]+A[j])

    for i in range(2*N):
        L = Sum[i]
        R = total / 10 + L
        #! 2分探索でRを探す
        flag = half_search(R,Sum)
        if flag:
            ans = 'Yes'
    print(ans)

if __name__ == '__main__':
    main()

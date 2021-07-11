

def judge(i,N):
    count0 = 0
    count1 = 0
    ans = []
    for n in range(N):
        bit = (i>>n)&1
        if bit == 0:
            count0 += 1
            ans.append('(')
        else:
            count1 += 1
            ans.append(')')
        if count1 < count0:
            return
    if count0 == count1:
        print(''.join(ans[::-1]))
        # print(i)
    else:
        return


def solve(N):
    for i in range(2**N):
        judge(i,N)

def main():
    N = int(input())
    if N % 2 == 0:
        solve(N)
    else:
        print('')

if __name__ == "__main__":
    main()

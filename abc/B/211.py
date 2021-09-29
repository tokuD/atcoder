def main():
    S = [input().rstrip() for i in range(4)]
    S = set(S)
    if len(S) == 4:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()

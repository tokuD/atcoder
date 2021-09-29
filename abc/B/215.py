def main():
    N = int(input())
    i = 0
    while True:
        if 2**i > N:
            print(i-1)
            exit()
        i += 1


if __name__ == '__main__':
    main()

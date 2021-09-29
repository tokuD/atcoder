def main():
    A,B = map(int,input().split())
    for i in range(256):
        if A ^ i == B:
            exit(print(i))



if __name__ == '__main__':
    main()

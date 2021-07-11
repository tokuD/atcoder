H,W = map(int,input().split())

if (H==1) or (W==1):
    print(H*W)
    exit()
else:
    print(((H+1)//2)*((W+1)//2))

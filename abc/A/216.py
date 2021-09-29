a = input()

xy = a.split('.')
x = xy[0]
y = xy[1]

if 0<=int(y)<=2:
    print("{}-".format(x))
elif 3<=int(y)<=6:
    print("{}".format(x))
else:
    print("{}+".format(x))

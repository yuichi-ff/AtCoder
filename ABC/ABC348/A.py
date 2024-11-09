N = int(input())

for i in range(1,N+1):#１から始まるんですよ……
    if i % 3 == 0:
        print("x",end="")
    else:
        print("o",end="")

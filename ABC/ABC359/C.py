Sx, Sy = map(int,input().split())
Tx, Ty = map(int,input().split())

if abs(Tx-Sx) <= 1 and Ty==Sy:
    if (Sx+Sy)%2 == 0 and Sx+1 == Tx:
        print(0)
        exit()
    elif (Tx+Ty)%2 == 0 and Tx+1 == Sx:
        print(0)
        exit()

if Sy == Ty:
    if (Sx+Sy)%2 == 0:
        print(abs(Sx-Tx)//2)
    else:
        print((abs(Sx-Tx)+1)//2)
    exit()

naname = abs(Sx-Tx)
tate = abs(abs(Ty-Sy)-naname)

print(naname+tate)
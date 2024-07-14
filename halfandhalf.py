A,B,C,X,Y = map(int,input().split())

ans = 1 << 30

for ab in range(0,min(A,B)*2,2):
    for a in range():
        a = X - ab
        b = 

        sm = a*A+b*B+ab*C
        ans = min(ans, sm)

print(ans)
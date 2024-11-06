M,D = map(int,input().split())
y, m, d = map(int,input().split())

if m==M and d==D:
    y+=1

if d==D:
    if m==M:
        m = 1
    else:
        m += 1

if d==D:
    d = 1
else:
    d += 1

print(y,m,d)
N,T,P = map(int,input().split())
L = list(map(int,input().split()))

# 冗長 かきなおす
ans = 0
for day in range(101):
    okcount = 0
    LL = L.copy()
    for i in range(len(L)):
        LL[i] += day
        if LL[i] >= T:
            okcount += 1

    if okcount >= P:
        ans = day
        break

print(ans)

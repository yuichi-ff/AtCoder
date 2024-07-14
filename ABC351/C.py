N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]

ans = 0

mxindex = 0
for i, ab in enumerate(AB):
    ans += ab[0]
    if AB[mxindex][1]-AB[mxindex][0] < ab[1]-ab[0]:
        mxindex = i

ans -= AB[mxindex][0]
ans += AB[mxindex][1]

print(ans)

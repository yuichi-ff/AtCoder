N = int(input())
AS = [input().split() for _ in range(N)]

ans = 0

LL = list(filter(lambda ass: ass[1] == 'L', AS))
RR = list(filter(lambda ass: ass[1] == 'R', AS))

for i in range(0,len(LL)-1):
    ans += abs(int(LL[i][0])-int(LL[i+1][0]))

for i in range(0,len(RR)-1):
    ans += abs(int(RR[i][0])-int(RR[i+1][0]))

print(ans)
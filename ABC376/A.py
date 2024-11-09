N,C = map(int,input().split())
T = list(map(int,input().split()))

ans = 1
ame = 0
for n in range(1,N):
    delay = T[n] - T[ame]
    if C <= delay:
        ans += 1
        ame = n

print(ans)
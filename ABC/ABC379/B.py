N, K = map(int,input().split())
S = input()

tooth = 0
ans = 0

for i in range(N):
    if S[i]=="O":
        tooth += 1
        if tooth == K:
            ans += 1
            tooth = 0
    else:
        tooth = 0

print(ans)
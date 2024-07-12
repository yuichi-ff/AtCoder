N = int(input())
S = input()

#print(S.count("ABC")) ずる

ans = 0
for i in range(2,N):
    if S[i-2:i+1] == "ABC":
        ans+=1

print(ans)
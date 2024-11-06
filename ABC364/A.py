N = int(input())
S = [input() for _ in range(N)]

ans = "Yes"
for i in range(0,N-1):
    if (i != N-2) and (S[i] == "sweet" and S[i+1] == "sweet"):
        ans = "No"
        break

print(ans)
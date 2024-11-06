S = input()

ans = set()

# 早めに解けたには解けたけど……
for i in range(len(S)):
    bubun = ""
    for j in range(i,len(S)):
        bubun += S[j]
        ans.add(bubun)

print(len(ans))


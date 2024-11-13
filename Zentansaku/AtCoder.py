S = input()

atgc = "ATGC"
i = 0
ans = 0
for s in S:
    if s in atgc:
        i+=1
    else:
        i=0
    ans = max(ans, i)

print(ans)
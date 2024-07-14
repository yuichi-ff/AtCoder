S = list(input())
SS = set(S)

ans = "Yes"

for i in range(1,100+1): # そうだね
    variation = 0
    for ss in SS:
        if S.count(ss) == i:
            variation += 1
    if variation != 2 and variation != 0:
        ans = "No"

print(ans)
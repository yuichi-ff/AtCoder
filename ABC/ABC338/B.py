S = input()

ans = []
mx = 0
for s in S:
    am = S.count(s)

    if am > mx:
        ans = []
        mx = am

    if am == mx:
        ans.append(s)

print(sorted(ans)[0])

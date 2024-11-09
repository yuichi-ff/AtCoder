"""
S = input()

d = ["dream","dreamer","erase","eraser"]

ans = "YES"
i = 0
while(i < len(S)):
    if S[i:i+7] in d:
        i += 7
    elif S[i:i+6] in d:
        i += 6
    elif S[i:i+5] in d:
        i += 5
    else:
        ans = "NO"
        break

print(ans) #エンエン
"""

S = input()[::-1]
d = [dd[::-1] for dd in ["dream","dreamer","erase","eraser"]]

ans = "YES"

temp = ""
i = 0
for s in S:
    temp += s
    if temp in d:
        temp = ""
        i = 0
    elif i > 7:
        ans = "NO"
        break
    i += 1

print(ans)
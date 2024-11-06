N = int(input())

#うわコードひどい

S = [input() for _ in range(N)]

sw, sh = (max([len(s) for s in S]), len(S))

tmp = [[" "]*sw for _ in range(sh)]

for i, s in enumerate(S):
    for j, s, in enumerate(s):
        tmp[i][j] = S[i][j]

for i in range(sh):
    for j in range(sw):
        if i == 0:
            continue
        if tmp[i][j] == " " and tmp[i-1][j] != " ":
            tmp[i][j] = "*"

ans = list(zip(*tmp[::-1]))

#zip(*配列[::-1])で転置可能
# zip(*aaa[::-1])
for an in ans:
    print(*an,sep="")
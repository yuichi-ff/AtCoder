N = int(input())
P = list(map(int,input().split()))
Q = int(input())
AB = [list(map(int,input().split())) for _ in range(Q)]

# N人ならんでるよー
# ならんでるひとはPiだよー

# Ai Biのどっちか前に並んでる方出力してねえ

ans = 0
for ab in AB:
    for i in range(N):
        if P[i] == ab[0] or P[i] == ab[1]:
            print(P[i])
            break


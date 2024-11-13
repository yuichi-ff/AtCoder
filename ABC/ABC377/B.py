Ss = [input() for _ in range(8)]

outpoints = []

for i in range(8):
    for j, s in enumerate(Ss[i]):
        if s == "#":
            outpoints.append([i,j])

ng = 0
for i in range(8):
    for j in range(8):
        for outpoint in outpoints:
            if i == outpoint[0] or j == outpoint[1]:
                ng += 1
                break

print((8*8)-ng)
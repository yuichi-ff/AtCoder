N,S,K = map(int,input().split())
PQ = [list(map(int,input().split())) for _ in range(N)]

gokei = 0
for p,q in PQ:
    gokei += p * q

if gokei < S:
    gokei += K
print(gokei)
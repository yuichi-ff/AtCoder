N = int(input())
qr = [list(map(int,input().split())) for _ in range(N)]
Q = int(input())
td = [list(map(int,input().split())) for _ in range(Q)]

# q で割ったあまりが r の日に回収
# t 種類 d ゴミが出る日
"""
for q in range(Q):
    t,d = td[q]
    q,r = qr[t-1]
    if d%q == r:
        print(d)
    else:
        print(r + ((d//q)*d)+(d%q)) ちがうねえ

"""

for q in range(Q):
    t,d = td[q]
    #print(f"d: {d}")
    q,r = qr[t-1]
    #print(f"q: {q},r: {r}")
    #t,d

    print( r + ((d - r + q - 1) // q) * q)
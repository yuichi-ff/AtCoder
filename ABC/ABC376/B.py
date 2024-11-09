N,Q = map(int,input().split())
HT = [list(input().split()) for _ in range(Q)]

hands = [1,2] #左手、右手

ans = 0
for ht in HT:
    ugokasu_te = 1 # 右手
    ugokasanai_te = 0
    if ht[0] == "L":
        ugokasu_te = 0 #左手
        ugokasanai_te = 1

    idousaki = int(ht[1]) #移動先

    # 右回転
    migi = 0
    for i in range(N):
        temp = (hands[ugokasu_te]+i) % N

        if temp == hands[ugokasanai_te]:
            migi = 9999999
            break
        if temp == idousaki:
            migi = i
            break
    # ←回転
    hidari = 0
    for i in range(N):
        temp = (hands[ugokasu_te]-i)
        if temp <= 0:
            temp = N+temp

        if temp == hands[ugokasanai_te]:
            hidari = 9999999
            break
        if temp == idousaki:
            hidari = i
            break
    
    hands[ugokasu_te] = idousaki

    ans += min(migi,hidari)

print(ans)
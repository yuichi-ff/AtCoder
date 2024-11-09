N,M = map(int,input().split())
KS = [list(map(int,input().split())) for _ in range(M)]
P = list(map(int,input().split()))

ans = 0

for bit in range(2 ** N): # ビット全探索用：ビットのパターン（スイッチのONOFFパターン）ごとにforで回す
    allon = True
    for i in range(M): # 電球ループ
        ons = 0 # オンの数
        for j in range(KS[i][0]):# スイッチループ
            ons += (bit >> KS[i][1+j]-1) & 1 # j番目のスイッチがonなら加算
        if ons % 2 != P[i]: # 電球が点灯しなければこのパターンはハズレ
            allon = False
    ans += allon

print(ans)
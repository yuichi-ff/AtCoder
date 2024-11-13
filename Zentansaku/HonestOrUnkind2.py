N = int(input())

XY = []
shougens = [[list(map(int,input().split())) for _ in range(int(input()))] for _ in range(N)]

mx = 0
for bit in range(2**N): # bit全探索
    honestsaying = [-1 for _ in range(N)] #「「正直者と仮定した人間」の証言」のリスト
    
    ok = True
    for n in range(N):
        if (bit>>n) & 1: #正直者と仮定したビットなら
            for x,y in shougens[n]: # 証言ループ用
                if honestsaying[x-1] != -1 and honestsaying[x-1] != y:
                    ok = False
                else:
                    honestsaying[x-1] = y


    for n in range(N):
        if honestsaying[n] == -1:
            continue
        if ((bit >> n) & 1) != honestsaying[n]: # 仮定と証言が矛盾したら
            ok = False

    if ok:
        mx = max(mx, bit.bit_count())

print(mx)
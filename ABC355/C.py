N,T = map(int,input().split())
A = list(map(int,input().split()))

inf = 1 << 30

bingo = [[inf]*N for i in range(N)]

for a in A:
    #aの配置された座標は？
    j, i = (a-1)%N, (a-1)//N
    print(a,i,j)
    bingo[i][j] = a

    mx = inf
    #横
    if max(bingo[i]) == a:
        mx = a
    #縦
    elif max([x[j] for x in bingo]) == a:
        mx = a
    
    if mx == a:
        print(a)
        exit()
K,G,M = map(int,input().split())

g,m = 0,0
for i in range(K):
    if g == G: # いっぱいなら飲む
        g = 0
    elif m == 0: # ないなら追加する
        m = M
    else:
        # マグカップが空になるか
        # グラスが水で満たされるまで
        # 水を移す
        #while (m == 0 or g == M):
        #    g += 1
        #    m -= 1
        # もしくは
        x = min(G-g,m)
        m -= x
        g += x
    
print(g,m)
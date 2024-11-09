N = int(input())
P = [list(map(int,input().split())) for _ in range(N)]

# １から始まるんですよ……

def distance(x0,y0,x1,y1): 
    # 今回の処理だと同点の場合があるので
    # 距離を問われていない場合、1/2乗すると危険・・・（不動点少数が不安定ですごい！）
    return ((x0-x1)**2)+((y0-y1)**2)

for i in range(N):
    mx = 0
    ans = 0
    for j in range(N):
        # 敗因：引数の順番
        # [i][j] [0][1]のどっちがxでどっちがyかちょっとわかってた方が良い
        dis = distance(P[i][0],P[i][1],P[j][0],P[j][1])
        if dis > mx:
            mx = dis
            ans = j
    print(ans+1)

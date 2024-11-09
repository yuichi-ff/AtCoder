H, W  = map(int,input().split())
Si, Sj = map(int,input().split())
mp = [input() for _ in range(H)] # 入力ミスってたあ こういう文字列入力のときはこうしよう
X = input()

# H, W たてよこ
# Si, Sj、 スタート地点、
# map まっぷ。 map[i][j]
# X 指示

def isInsideOfMap(i,j):
    return not (i<0 or i>H-1 or j<0 or j>W-1)

tloc = [Si-1, Sj-1]
for x in X:
    if x == "U":
        if isInsideOfMap(tloc[0]-1,tloc[1]):
            if mp[tloc[0]-1][tloc[1]] == ".":
                tloc[0]-=1

    elif x =="D":
        if isInsideOfMap(tloc[0]+1,tloc[1]):
            if mp[tloc[0]+1][tloc[1]] == ".":
                tloc[0]+=1

    elif x =="R":
        if isInsideOfMap(tloc[0],tloc[1]+1):
            if mp[tloc[0]][tloc[1]+1] == ".":
                tloc[1]+=1

    elif x == "L":
        if isInsideOfMap(tloc[0],tloc[1]-1):
            if mp[tloc[0]][tloc[1]-1] == ".":
                tloc[1]-=1

print(tloc[0]+1,tloc[1]+1)
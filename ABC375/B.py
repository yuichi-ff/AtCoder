import math

N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]
XY.insert(0,[0,0])
XY.append([0,0])

#print(XY)

def score(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

ans = 0
for i in range(len(XY)-1):
    xy1=XY[i]
    xy2=XY[i+1]
    ans += score(xy1[0],xy1[1],xy2[0],xy2[1])

print(ans)
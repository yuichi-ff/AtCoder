N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]

tx,ty = (0,0)
for x,y in XY:
    tx += x
    ty += y

ans = "Draw"
if tx>ty:
    ans = "Takahashi"
elif tx<ty:
    ans = "Aoki"

print("Takahashi" if tx>ty else "Aoki")
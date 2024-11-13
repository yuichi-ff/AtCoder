H, W, N = map(int, input().split())

FIELD = [[False] * W for _ in range(H)]  # False 白(.)

directions = ("U", "R", "D", "L")  # 加算で90、減算で-90
direction = 0
loc = [0, 0] # Y,X（i,j)です…… これでWA 気をつけよう

for i in range(N):

    if not FIELD[loc[0]][loc[1]]:  # 白（.）なら
        FIELD[loc[0]][loc[1]] = True
        direction = (direction + 1) % 4  # 90度回転
    else:
        FIELD[loc[0]][loc[1]] = False
        direction = (direction - 1) % 4  # -90度回転

    if directions[direction] == "U":
        loc[0] = (loc[0] - 1) % H
    elif directions[direction] == "D":
        loc[0] = (loc[0] + 1) % H
    elif directions[direction] == "R":
        loc[1] = (loc[1] + 1) % W
    elif directions[direction] == "L":
        loc[1] = (loc[1] - 1) % W

    #print(i + 1, directions[direction], loc)

for field in FIELD:
    for ff in field:
        print("#" if ff else ".", end="")
    print("")

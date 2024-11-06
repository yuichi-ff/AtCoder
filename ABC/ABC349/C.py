S = input()+"X"
T = input()

# 解説見た後の所感
# １．Tの末尾Xを消す
# ２．Sの末尾にXを足す

ans = "No"
l = 0 # T[l] → 判定中の文字
for i in range(len(S)):
    if l == 2:
        if T[l] == S[i].upper(): 
            ans = "Yes"
            break
    elif T[l] == S[i].upper():
        l+=1

print(ans)

# S: 10^5
# forは１回程度まで

# ３文字大文字
# or
# ２文字の後にX が空港コード か判定してね という問題

# 【例】
# narita
# NRT
# losangeles
# LAX

# xyz
# XZX で引っかかっている

# AC獲得

# 二文字目が末尾、かつ最後がXの場合を追加しておわり
# これテストケース見れたからいいけど本番だと無理……
"""
ans = "No"
l = 0
# T[l] → 判定中の文字
for i in range(len(S)):
    if l == 2:
        if T[l] == "X" or T[l] == S[i].upper(): 
            ans = "Yes"
            break
    elif T[l] == S[i].upper():
        l+=1

if l == 2 and T[l] == "X":
    ans = "Yes"

print(ans)

"""
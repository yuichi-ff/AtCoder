S = input()

"""
for i in range(len(S)-1):
    if S[i] != S[i-1] and S[i] != S[i+1]:
        print(i+1)
        # aab とかの場合に無理（最後のbが無理）
"""

for i in range(len(S)):
    if S.count(S[i]) == 1:  # 他のどの文字とも異なる文字は前から何文字目でしょうか。
                            # →１度だけ出てくるやつを答えればいいと
        print(i+1)
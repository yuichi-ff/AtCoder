N = int(input())
CA = [list(reversed(list(map(int,input().split())))) for _ in range(N)]


# やっていきましょう
# オーダーは2×10^5、forは１回

# 最小値の最大値、言い換えれば
# 最もリスクの少ない色を選べって感じ

"""
100 1
20 5
30 5
40 1

↓ sort

1 40 -> maxに代入
1 100
5 20 -> maxに代入
5 30
"""

CA.sort()

currentTaste = CA[0][0]
mx = CA[0][1]

for i in range(len(CA)):
    if currentTaste != CA[i][0]:
        mx = max(mx, CA[i][1])
        currentTaste = CA[i][0]

print(mx)
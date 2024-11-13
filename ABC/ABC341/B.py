N = int(input())
A = list(map(int,input().split()))
ST = [list(map(int,input().split())) for _ in range(N-1)]

# Nつ国がある
# 国iの通貨をAi円持ってる

# i: 1~N-1国の通貨をSi以上持ってた場合
# iの通貨をSi円払って、i+1国の通貨をTi円もらう

# 最後に持ってるN国の通貨の単位数の最大値を出力しろ

"""
4
5 7 0 3
2 2
4 3
5 2

→
5//2 = 2

i: 5%2==1
i+1: i+1 + (5//2)*2

1 11 0 3
4 3

1 3 6 3
5 2

1 3 1 5
"""

# 問題文ややこしいけど割とそのまま？

# N <= 2*10^5
# １，２回は間に合う

for i in range(N-1):
    A[i+1] = A[i+1] + (A[i]//ST[i][0]) * ST[i][1]

print(A[-1])
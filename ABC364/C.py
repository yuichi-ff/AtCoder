N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# 初C AC！！！！！！！！やったあああああああああああああ

# 1≤N≤2×10^5
# forは２回いけるか

# 4 7 18
# 2 3 5 1:A
# 8 8 1 4:B

# 2
# 2,3,1,4で食べると2,3の時点でAが8を超える

# 大きい順に並べる？ ソートしたら順序残らない
# → 求められてるのは皿の個数なので順序は必要でない？

A = sorted(A)
B = sorted(B)

Asum = 0
Bsum = 0

ans = 0
for i in range(N-1,-1,-1):
    Asum += A[i]
    Bsum += B[i]
    ans += 1
    if Asum > X or Bsum > Y:
        break

print(ans)
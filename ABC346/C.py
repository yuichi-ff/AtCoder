# from sortedcontainers import SortedSort

N, K = map(int,input().split())
A = set(list(map(int,input().split())))

# むずかしそー
# 1～K のうち、いちどもAにあらわれないのを合算してね
# → Aに現れるのを合算して引く？

# 1≤N≤2×10^5
# 1≤K≤2×10^9

# KをループするとTLEなる

# 4 5
# 1 6 3 1
# 2+4+5=11

# 1+3=10（あらわれたやつ）
# 1/2*n*(n+1)
# 1/2 * 4 * 5 = 10（１から５までの合計）

Ksum = int((K*(K+1))//2)

appearedSum = 0
for a in A:
    if a <= K:
        appearedSum += a

print(Ksum - appearedSum)
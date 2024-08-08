N,M = map(int,input().split())
A = list(map(int,input().split()))

# N: 2*10^5 forは１回となんかその他ちょい
# M: 2*10^14

# 総当たりは無理
# 1 3 2 4
# ソートすると
# 1 2 3 4
"""
SA = sorted(A)

if sum(A) <= M:
    print("infinite")
    exit()

ans = 0
for n in SA:
    if sum(min(n,a) for a in A) <= M:
        ans = n

print(ans)"""


if sum(A) <= M:
    print("infinite")
    exit()

ok = 0
ng = max(A)

while ok+1 < ng:
    mid = (ok + ng) // 2
    if sum(min(mid,a) for a in A) <= M:
        ok = mid
    else:
        ng = mid

print(ok)

# for a in A:
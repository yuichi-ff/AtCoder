N = int(input())
A = list(map(int,input().split()))

#正解例
"""
stack = []
for a in A:
    stack.append(a)
    for i in range(N):
        if len(stack) >=2 and stack[-1] == stack[-2]:
            stack[-2] = stack[-2]+1
            del stack[-1]
        else:
            break
print(len(stack))
"""

# C問題でも言われたまま実装する系が出る、ということですね

# 全通り試すと最大4 x 10^10になるのでTLE多分
# いや 4x10^10にはならない
"""
rinsetuindex = 1
for j in range(len(A)):
    for i in range(len(A)-1):
        if A[i+rinsetuindex] == -1:
            rinsetuindex += 1
            continue
        elif A[i] != A[i+rinsetuindex]:
            rinsetuindex = 1
            continue

        A[i] = A[i]+1
        A[i+1] = -1
        rinsetuindex = 1
"""
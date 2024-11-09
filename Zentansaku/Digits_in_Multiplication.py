import math
N = int(input())
INF = 1 << 30

def dig(n):
    digit = 0
    while(n > 0):
        n = n//10
        digit+=1
    return digit

def F(a,b):
    return max(dig(a),dig(b))

"""
ans = 999999999999999999999999999999
for a in range(1,(10**5)+1):
    if N % a == 0:
        b = N / a
        ans = min(F(a,b),ans)
"""

#高速化畳
ans = INF
for a in range(1,int(math.sqrt(N))+1):
    if N % a == 0:
        b = N / a
        ans = min(F(a,b),ans)

print(ans)

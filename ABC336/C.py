N = int(input())
A = list(map(int,input().split()))
#なんでえ
"""
A.insert(0,0)

between = []
for i in range(1,N):
    between.append(A[i-1]+A[i])

mn = abs(min(between))

print(mn + sum(A))"""

passengers = 0
saishou = 0
for a in A:
    passengers += a
    saishou = min(passengers, saishou)

print(abs(saishou) + passengers)
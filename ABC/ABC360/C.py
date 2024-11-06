N = int(input())
A = list(map(int,input().split()))
W = list(map(int,input().split()))

"""
tyofukusu = len(A) - len(set(A))

W_sorted = sorted(W)

cost = 0
for i in range(tyofukusu):
    cost += W_sorted[i]"""

AW = sorted(list(zip(A,W)))

cost = 0
aset = set(A)
index = 0

for i in range(len(aset)):
    j = aset[i]
    cost += max(AW[:j])

print(sum(W) - cost)
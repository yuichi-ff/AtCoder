N,M = map(int,input().split())

A = list(map(int,input().split()))
X = [list(map(int,input().split())) for _ in range(N)]
SUM = [0 for _ in range(M)]

for x in X:
    for m in range(M):
        SUM[m] += x[m]

ans = "Yes"
for m in range(M):
    if SUM[m] < A[m]:
        ans = "No"
        break

print(ans)
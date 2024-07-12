N,A = map(int,input().split())
T = list(map(int,input().split()))

T[0] += A
for i in range(1,N):
    if T[i-1] > T[i]:
        T[i] = T[i-1]+A
    else:
        T[i]+=A

for t in T:
    print(t)
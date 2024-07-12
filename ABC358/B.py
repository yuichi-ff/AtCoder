N,A = map(int,input().split())
T = list(map(int,input().split()))

addedT = [t + A for t in T]

for i in range(1,N-1):
    if addedT[i]-addedT[i-1] < A:
        addedT[i] = addedT[i-1]+A

for t in addedT:
    print(t)
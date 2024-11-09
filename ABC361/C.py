N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))

for k in range(K):
    if (A[-2] - A[0]) < (A[-1] - A[1]):
        del A[-1]
    else:
        del A[0]

print(A[-1]-A[0])
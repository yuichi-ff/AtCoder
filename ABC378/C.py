N = int(input())
A = list(map(int,input().split()))
B = {}

for i in range(N):
    print(B.get(A[i],-1),end=" ")
    B[A[i]] = i+1
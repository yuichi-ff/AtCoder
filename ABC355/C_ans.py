N,T = map(int,input().split())
A = list(map(int,input().split()))

inf = 1 << 30

mat = [[inf]*N for i in range(N)]

for i in range(T):
    c,r = A[i]//N, A[i]%N
    mat[c][r] = i+1


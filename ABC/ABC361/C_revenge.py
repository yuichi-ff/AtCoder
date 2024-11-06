N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))
INF = 1 << 30

ans = INF
for i in range(K+1):
    ans = min(ans, A[i+(N-K-1)] - A[i])

print(ans)
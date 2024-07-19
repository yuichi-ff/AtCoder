N = int(input())
A = list(map(int,input().split())) # 入ってる箱
W = list(map(int,input().split())) # 重さ

b = [0 for _ in range(N+1)]

for i in range(N):
    A[b[i]] = max(A[b[i]],W[i])

print(sum(W)-sum(b))#????
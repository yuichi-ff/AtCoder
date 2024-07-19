N = int(input())
A = list(map(int,input().split()))
W = list(map(int,input().split()))

cost = 0
maxcosts = [0 for _ in range(N)]

for i in range(N):
    i_box = A[i]-1
    weight = W[i]
    maxcosts[i_box] = max(maxcosts[i_box],weight)

print(sum(W) - sum(maxcosts))
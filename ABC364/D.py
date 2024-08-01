N, Q  = map(int,input().split())
A = list(map(int,input().split()))

BK = [list(map(int,input().split())) for _ in range(Q)]

# BK[Qindex][0->b,1->k]
# 1 ≤ N,Q ≤ 10^5
# ２重for -> 10^10になるのでTLE
# sortは多少使ってもよさそう

# まあD問題だしTLEしてもいいからとりあえず実装してみるか……
# なんか方法があるんだろうな

for bi in range(Q):
    distances = []
    for ai in range(N):
        dist = abs(BK[bi][0] - A[ai])
        distances.append(dist)

    distances.sort()
    print(distances[BK[bi][1]-1])
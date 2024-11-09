Q = int(input())
QL = [list(map(int,input().split())) for _ in range(Q)]

A = []

for ql in QL:
    if ql[0] == 1:
        A.append(ql[1])
    elif ql[0] == 2:
        print(A[-ql[1]])
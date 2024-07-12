N,M,K = map(int,input().split())

T_MASK = [1 for _ in range(N)]
F_MASK = [0 for _ in range(N)]
FINAL_MASK = [0 for _ in range(N)]

for m in range(M):
    line = input().split()
    A = list(map(int,line[1:-1]))
    if line[-1] == "o":
        for a in A:
            T_MASK[a-1] = 0 if T_MASK[a-1] == 1 else 1
        
    elif line[-1] == "x":
        for a in A:
            F_MASK[a-1] = 0 if F_MASK[a-1] == 0 else 1

for i in range(N):
    FINAL_MASK[i] = T_MASK[i] + F_MASK[i]

print(FINAL_MASK.count(1))
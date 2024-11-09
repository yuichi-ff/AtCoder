import copy
N = int(input())

mat = [list(input()) for _ in range(N)]
new_mat = copy.deepcopy(mat)


for i in range(1,(N//2)+1):
    new_mat = copy.deepcopy(mat)
    for x in range(i,N+1-i+1):
        for y in range(i,N+1-i+1):
            #print(f"order:{x},{y}:")
            #print(f"  {y},{N+1-x}: {mat[y-1][N+1-x-1]}")
            #print(f"           ↑ で置き換え ")
            #print(f"  {x},{y}:{mat[x-1][y-1]}")
            new_mat[y-1][N+1-x-1] = mat[x-1][y-1]
    mat = copy.deepcopy(new_mat)

for line in new_mat:
    print(*line,sep="")
import itertools

N = int(input())
XYs = [list(map(int,input().split())) for _ in range(N)]

XY_p = list(itertools.permutations(XYs))

sm = 0
for permutation in XY_p:
    distance = 0
    for i in range(1,len(permutation)):
        point_c = permutation[i]
        point_b = permutation[i-1]
        distance += pow(((point_c[0]-point_b[0])**2+(point_c[1]-point_b[1])**2),1/2)
    sm += distance

print(str(sm/len(XY_p)))
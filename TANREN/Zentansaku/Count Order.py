import itertools

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

permutations = list(itertools.permutations([n+1 for n in range(N)]))

#print(abs(permutations.index(P)-permutations.index(Q)))
#exit()
p = 0
q = 0
for i,permutation in enumerate(permutations):
    if permutation == P:
        p = i
    if permutation == Q:
        q = i

print(abs(p-q))
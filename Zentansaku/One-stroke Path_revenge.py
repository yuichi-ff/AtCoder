import itertools

N,M = map(int,input().split())
As = [list(map(int,input().split())) for _ in range(N)]

permutations = list(itertools.permutations([i+1 for i in range(N)]))


ans=0
for permutation in permutations:

    ok = True
    for i in range(len(permutation)-1):
        path = [permutation[i],permutation[i+1]]
        if path in As:
            ok = False
    if ok:
        ans += 1

print(ans)
import itertools

N,M = map(int,input().split())
As = [list(map(int,input().split())) for _ in range(N)]

permutations = list(itertools.permutations([i+1 for i in range(N)]))

ans = 0
for permutation in permutations:
    if permutation[0] != 1:
        continue

    ok = True
    for i in range(len(permutation)-1):
        path_1 = [permutation[i],permutation[i+1]]
        path_2 = [permutation[i+1],permutation[i]]
        if not ((path_1 in As) or (path_2 in As)):
            ok = False

    if ok:
        ans += 1

print(ans)
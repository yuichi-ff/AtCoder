import itertools

N,M = map(int,input().split())
S = [input() for _ in range(N)]

ans = []
ptn = list(itertools.permutations(S))

for p in ptn:
    i = 0
    combined = ["×" for _ in range(M)]
    for pp in p:
        combined = ["o" if p == "o" else c for (c, p) in zip(combined, pp)]
        i+=1
        if combined.count("o") >= M:
            ans.append(i)

print(min(ans))
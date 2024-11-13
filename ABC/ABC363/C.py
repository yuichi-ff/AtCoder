import itertools

N,K = map(int,input().split())
S = input()

# 普通に最初のやり方で合ってたという……ｗ
# 単純にpythonだと遅いので無理です＾＾ってことらしい

#permutations = set(itertools.permutations(S)) #TLEる
#print(len(permutations),permutations) 
#print(permutations)
"""
# 「与えられた文字列の中から」K文字の回分列挙してマッチするか調べたほうが早いな
# 問題は、やり方がわからないこと 一体どうすれば……！？
#　無知は罪 ムチムチになる
# combination使えば良い
combinations = itertools.combinations(S,K)

combs = []
mojiz = 0
for comb in combinations:
    if comb == comb[::-1]:
        combs.append(comb)
print(combs) """

# まだTLEなんですか！？ → 10 2 abcdefghijkとかTLEなる
"""fukumu = 0
for permutation in permutations:
    includeskaibun = False
    for i in range(len(permutation)-K+1):
        judge = permutation[i:i+K]
        if judge == judge[::-1]:
            #print(permutation, judge,"is kaibun")
            includeskaibun = True

    if includeskaibun:
        fukumu += 1
print(N - fukumu)
"""
"""
def isparry(s):
    for i in range(len(s)//2):
        if S[i] == S[-i]:
            return False
        return True

fukumu = 0
for permutation in permutations:
    includeskaibun = False
    for i in range(len(permutation)-K+1):
        if isparry(permutation[i:i+K]):
            includeskaibun = True

    if includeskaibun:
        fukumu += 1"""
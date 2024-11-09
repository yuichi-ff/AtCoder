S = input()

u = len([s for s in S if s.isupper()])
l = len([s for s in S if s.islower()])

print(S.upper() if u > l else S.lower())
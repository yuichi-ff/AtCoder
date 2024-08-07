S = input()

#なにげにここの()のif思いつかん
print("Yes" if S[0].isupper and (len(S) == 0 or S[1:].islower()) else "No")
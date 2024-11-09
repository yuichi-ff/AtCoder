S = list(input())
T = list(input())

X = []

diffN = 0
for ii in range(len(S)):
    if S[ii] != T[ii]:
        diffN+= 1

for i in range(diffN):

    temp_arr = []
    for j in range(len(S)):
        tempS = S.copy()
        if tempS[j] != T[j]:
            tempS[j] = T[j]
            temp_arr.append("".join(tempS))
    #print(temp_arr)
    f = min(temp_arr)
    X.append(f)
    S = list(f)

print(len(X))
for xx in X:
    print(xx)
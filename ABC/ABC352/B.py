S = input()
T = input()

i = 0
for j,t in enumerate(T):
    if t == S[i]:
        print(j+1, end=" ")
        i+= 1
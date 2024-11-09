S,T = input().split()

for w in range(1,len(S)):
    loopcount = len(S)//w if len(S)%w == 0 else len(S)//w+1
    child = []
    for i in range(loopcount):
        child.append(S[i*w:(i*w)+w].ljust(w, " "))

    for i in range(w):
        ans = ""
        for c in child:
            ans += c[i] if c[i] != " " else ""
        if ans == T:
            print("Yes")
            exit()

print("No")
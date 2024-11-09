N,X,Y,Z = map(int, input().split())

res = "No"
if X > Y:
    if Y <= Z and Z <= X:
        res = "Yes"
else:
    if X <= Z and Z <= Y:
        res = "Yes"

print(res)
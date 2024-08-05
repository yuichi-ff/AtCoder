R,G,B = map(int, input().split())
C = input()

ans = 0
if C == "Blue":
    ans = min(R,G)
elif C == "Green":
    ans = min(R,B)
elif C == "Red":
    ans = min(B,G)

print(ans)
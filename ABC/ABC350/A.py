S = input()

num = int(S[3:])

if (0 < num and num < 350) and num != 316:
    print("Yes")
    exit()

print("No")
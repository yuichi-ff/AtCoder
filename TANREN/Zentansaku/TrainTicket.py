V = list(map(int,input()))

for i in range(2**3):
    ans = V[0]
    ops = []
    for bit_shift in range(3):
        if (i>>bit_shift) & 1:
            ans += V[bit_shift+1]
            ops.append("+")
        else:
            ans -= V[bit_shift+1]
            ops.append("-")
    if ans == 7:
        print(f"{V[0]}{ops[0]}{V[1]}{ops[1]}{V[2]}{ops[2]}{V[3]}=7")
        exit()
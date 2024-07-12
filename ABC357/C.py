Lv = int(input())

ans = [["#"] * (3**Lv) for _ in range(3**Lv)]

carpets = []

for lv in range(Lv):
    carpet=[["#"] * (3**lv) for _ in range(3**lv)]

    for i in range(3**lv):
        for j in range(3**lv):
            if i//(3**(lv-1)) == 1 and j//(3**(lv-1)) == 1:
                carpet[i][j]="."

    carpets.append(carpet)



for c in carpets:
    for i in range(len(c)):
        print(*c[i])

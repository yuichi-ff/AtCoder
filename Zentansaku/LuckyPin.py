N = int(input())
S = input()

ans = set()
for i in range(1000):
    pin = str(i).zfill(3) # -> "000~999"
    pin_i = 0

    found = ""
    for s in S:
        if pin[pin_i] == s:
            pin_i+=1
            found+=s
        if len(found) == 3:
            ans.add(found)
            break

print(len(ans))
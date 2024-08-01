a = []
while True:
    i = input()
    a.append(i)
    if i == "0":
        break

for s in a[::-1]:
    print(s)
exit()

a = []
ok = True
while ok:
    i = int(input())
    if i == 0:
        ok = False
    a.append(i)

a.reverse()
for i in a:
    print(i)

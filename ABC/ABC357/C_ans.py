A = ["#"]

for _ in range(int(input())):
    x = [a * 3 for a in A]
    y = [a + "." * len(a) + a for a in A]
    print("x+y", x + y + x)
    A = x + y + x

print("\n".join(A))
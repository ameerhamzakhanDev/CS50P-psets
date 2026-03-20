import sys
x, y, z = input("Expression: ").strip().split()

if not (x.isdigit() and z.isdigit()):
    print("Enter a simple expression like: 2 + 2")
    sys.exit()

x = int(x)
z = int(z)

if y == "+":
    print(f"{float(x + z):.1f}")
elif y == "-":
    print(f"{float(x - z):.1f}")
elif y == "*":
    print(f"{float(x * z):.1f}")
elif y == "/":
    if y == 0:
        print("Cannot divide with 0")
        sys.exit()
    print(f"{float(x / z):.1f}")
else:
    print("Operator not available")


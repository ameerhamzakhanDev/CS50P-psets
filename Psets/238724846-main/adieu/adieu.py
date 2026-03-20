import inflect

names = []
p = inflect.engine()

while True:
    try:
        name = input("Enter a name: ")
        print(name)
    except EOFError:
        print("")
        break
    names.append(name)
    print(names)

print(f"Adieu, adieu, to {p.join(names)}")

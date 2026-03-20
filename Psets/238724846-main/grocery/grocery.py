
items = {}
i = 0
while True:
    try:
        item = input("").strip().upper()

    except EOFError:
        for i, a in sorted(items.items(), key= lambda x: x[0]):
            print(f"{a} {i}")
        break

    for itm, amount in items.items():
        if item == itm:
             items[item] = int(items[item]) + 1
    if not item in items.keys():
        items.update({item: 1})




greeting = input("Geeting: ")


if "hello" in greeting.lower() or "hello," in greeting.lower():
    print("$0")
elif greeting.lower().index("h") == 0:
    print("$20")
else:
    print("$100")

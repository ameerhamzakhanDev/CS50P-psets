
ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()

if ans == "42":
    print("Yes")
elif ans.lower() == "forty two" or ans.lower() == "forty-two":
    print("Yes")
else:
    print("No")

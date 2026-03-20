def main():
    initial =  input("Input: ")
    print(f"Output: {shorten(initial)}")

def shorten(inpts):
    result = ""
    for inpt in inpts:
        inptL = inpt.lower()
        if inptL == "a" or inptL == "i" or inptL == "o" or inptL == "e" or inptL == "u":
            pass
        else:
            result += inpt
    return result

if __name__ == "__main__":
    main()

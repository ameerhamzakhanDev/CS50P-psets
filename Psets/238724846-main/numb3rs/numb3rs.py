import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"


    matches = re.search(pattern, ip)


    if matches:
        for mach in matches.groups():

            if len(mach) > 1 and mach.startswith("0"):
                return False
            elif int(mach) < 256:
                print(len(mach))
                pass
            else:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()

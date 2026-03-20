import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str):

    pattern = r"^<iframe.+src=\".*youtube\.com/embed/(?P<id>\w{11}).+</iframe>$"

    matches = re.search(pattern, s, re.DOTALL)

    if matches:
        url = f"https://youtu.be/{matches.group("id")}"
        return url
    else:
        return None





if __name__ == "__main__":
    main()

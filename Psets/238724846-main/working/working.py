import re


def main():
    print(convert(input("Hours: ")))


def convert(s):

    pattern = r"(?P<hours>[\d\:]{1,5}) (?P<start_time>(AM|PM)) to (?P<mins>[\d\:]{1,5}) (?P<end_time>(AM|PM))"

    matches = re.search(pattern, s, re.IGNORECASE)
    if matches:

        start_hour = matches.group("hours").split(":")
        end_hour = matches.group("mins").split(":")
        start_time = matches.group("start_time")
        end_time = matches.group("end_time")

        if int(start_hour[0]) > 12 or int(end_hour[0]) > 12:
            raise ValueError("Given time was not correct")


        # First part of time's logic
        if start_time == "AM":
            if start_hour[0] == "12":
                start_hour[0] = "00"
            else:
                start_hour[0] = f"{int(start_hour[0]):02}"

        elif int(start_hour[0]) == 12:
            pass

        else:
            start_hour[0] = int(start_hour[0]) + 12

        if len(start_hour) == 1:
            start_hour.append("00")


        # First part of time's logic
        if end_time == "AM":
            if end_hour[0] == "12":
                end_hour[0] = "00"
            else:
                end_hour[0] = f"{int(end_hour[0]):02}"

        elif int(end_hour[0]) == 12:
            pass

        else:
            end_hour[0] = int(end_hour[0]) + 12

        if len(end_hour) == 1:
            end_hour.append("00")

        if int(start_hour[1]) >= 60 or int(end_hour[1]) >= 60:
            raise ValueError("Given time was not correct")

        if len(start_hour[1]) >= 3 or len(end_hour[1]) >= 3:
            raise ValueError("Given time was not correct")


        return f"{start_hour[0]}:{start_hour[1]} to {end_hour[0]}:{end_hour[1]}"

    else:
        raise ValueError("Given time was not correct")







if __name__ == "__main__":
    main()

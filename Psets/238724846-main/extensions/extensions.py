
extension = input("File name: ").strip().lower()

if not ("." in extension):
     print("application/octet-stream")

if ("." in extension):
    if (".gif" in extension or ".jpeg" in extension or ".png" in extension):
        extension =  extension.split(".")
        print(f"image/{extension[1]}")

    elif ".jpg" in extension:
        print ("image/jpeg")

    elif ".zip" in extension:
        print("application/zip")

    elif ".pdf" in extension:
        print("application/pdf")


    elif ".txt" in extension:
        print("text/plain")

    else:
        print("application/octet-stream")



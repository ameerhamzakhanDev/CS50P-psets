import requests as req
import sys


if len(sys.argv) == 1:

    sys.exit("Missing command-line argument")

if not (lambda string: True if string.replace('.', '', 1).isdigit() else False):
    sys.exit("Command-line argument is not a number ")

try:
    response = req.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=06153537e0b7d018bb564886148da386d9984dac5d6ab99251daa0742dfc1605")


except req.RequestException:
    print("An API error occured")

contents = response.json()

for key, value in contents["data"].items():
    if key == "priceUsd":
        value = float(value) * float(sys.argv[1])
        print(f"${value:,.4f}")

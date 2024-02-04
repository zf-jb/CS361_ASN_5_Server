# Adapted from example in HTTP request documentation @ https://pypi.org/project/requests/

import requests


def get_message():
    response = requests.get('http://127.0.0.1:8080/get_message')    # local host default port
    if response.status_code == 200:     # HTTP OK Message
        print(f"{response.json()['response']}")


if __name__ == '__main__':
    get_message()
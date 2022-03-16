
import requests

if __name__ == '__main__':
    response = requests.get("https://www.bbc.co.uk")
    print(response)
    print(response.status_code)
    print(response.content)
    print("--------------------------------")
    print(response.headers)


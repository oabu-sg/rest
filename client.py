
import requests

if __name__ == '__main__':
    response = requests.get("https://api.postcodes.io/postcodes/EC2Y5AS")
    print(response)
    print(response.status_code)
    print("---------Content ---------")
    print(response.content)
    print("------------JSON ----------")
    print(response.json())
    print("--------------------------------")
    print(response.headers)


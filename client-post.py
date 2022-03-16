import requests
import json

if __name__ == "__main__":
    data_dict = {'postcodes': ['EC2Y5AS', 'EX165BL', 'W25AA']}

    data_json = json.dumps(data_dict)
    headers_dict = {'Content-Type': 'application/json'}

    response = requests.post("https://api.postcodes.io/postcodes", data = data_json, headers = headers_dict)
    print("------------Status Code ----------")
    print(response.status_code)

    print("------------JSON ----------")
    print(response.json())
import simplejson as json
import requests


def main():
    # https://reqres.in/api/users?page=1
    params = {"page": 1}
    response = requests.get("https://reqres.in/api/users", params)
    data = {
        "statusCode": response.status_code,
        "url": response.url,
        "content": json.loads(response.content)
    }
    
    print(data)
    file = open("result.json", "w+")
    file.write(json.dumps(data))


main()
import simplejson as json
import requests


def main():
    response = requests.get("https://reqres.in/api/users?page=1")
    data = {
        "statusCode": response.status_code,
        "url": response.url,
        "content": json.loads(response.content)
    }
    
    print(data)
    file = open("result.json", "w+")
    file.write(json.dumps(data))


main()
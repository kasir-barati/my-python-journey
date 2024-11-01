import simplejson as json
import requests
from io import BytesIO
from PIL import Image
from .types.create_user import CreateUser


def fetchJsonData(url: str) -> None:
    params = {"page": 1}
    response = requests.get(url, params)
    data = {
        "statusCode": response.status_code,
        "url": response.url,
        "content": json.loads(response.content)
    }
    
    print(data)
    file = open("result.json", "w+")
    file.write(json.dumps(data))


def download_picture(url: str) -> None:
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error occurred with {response.status_code}")
    
    """
    response.content:
      - Content of what it did get from the URL in byte
      - We have to convert it anyway as we did in fetchJsonData
    BytesIO:
    - The optional argument is a bytes-like object that contains initial data.
      - bytes-like example: b"abcdef"
    - Returns A binary stream.
    - The buffer is discarded when the close() method is called.
      - Which in this case will never be called
    """
    image = Image.open(BytesIO(response.content))

    print(image.size, image.format, image.mode)

    path = f"image.{image.format}"

    try:
        image.save(path, image.format)
    except IOError:
        print("Cannot save file")


def create_user(url: str, data: CreateUser) -> None:
    """
    We do not need to specify the data type as it is detected by requests
    and the proper http content-type header would be settled.
    """
    response = requests.post(url, data)
    
    """
    The response.content is 
      b'{"name":"Kasir","job":"Fullstack developer in Germany","id":"175","createdAt":"2022-06-29T15:53:28.988Z"}'
    as you know we can deserialize it with json.loads
    """
    print(json.loads(response.content))

fetchJsonData("https://reqres.in/api/users")
download_picture("https://mcdn.wallpapersafari.com/medium/79/6/BcX5K7.jpg")
create_user(
    "https://reqres.in/api/users", 
    {
        "name": "Kasir",
        "job": "Fullstack developer in Germany"
    }
)


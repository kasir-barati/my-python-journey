import os
import simplejson as json


my_file = open("/tmp/new-file.md", "w", encoding="utf8")
message = "This is Kasir, talking to you from his own VSCode."
my_file.write(message)


def main():
    read_json_file('sample.json')


def read_json_file(file_name):
    if os.path.isfile(file_name) and os.stat(file_name).st_size != 0:
        old_file = open(file_name, "r+")
        old_file_content = old_file.read()
        data = json.loads(old_file_content)
        print(f"Current age is {data['age']}")
        data['age'] += 1
        print(f"Age is {data['age']}")
        old_file.seek(0)
    else:
        old_file = open(file_name, "w+")
        data = {
            "name": "Kasir",
            "age": 27
        }
        print(f"Age is {data['age']}")

    old_file.write(json.dumps(data))


main()
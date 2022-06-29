my_file = open("/tmp/new-file.md", "w", encoding="utf8")

message = "This is Kasir, talking to you from his own VSCode."

my_file.write(message)
# Help in opening URLs (mostly HTTP)
import urllib.request

# In this case it returns an HTTPResponse object which can work as a context manager.
response = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in response:
    decoded_line = line.decode().strip()
    print(decoded_line)

print("\r\n\r\n")

response = urllib.request.urlopen("http://www.dr-chuck.com/page1.html")
for line in response:
    decoded_line = line.decode().strip()
    print(decoded_line)

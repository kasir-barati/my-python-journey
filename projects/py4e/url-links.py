import re
from bs4 import BeautifulSoup
from urllib import request
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# We can use:
# - http://www.dr-chuck.com/page1.html
# - https://www.linkedin.com/jobs/
url = input("Enter URL address: ")

url_re = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    # domain...
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def is_url(url_address):
    result = url_re.match(url_address)

    return result != None


if (not is_url(url)):
    raise Exception("URL is invalid!")

# We are reading it all in one go, it is OK as long as it is not so large
html_document = request.urlopen(url, context=ssl_context).read()
beautiful_soup = BeautifulSoup(html_document, "html.parser")
anchor_tags = beautiful_soup('a')
links = []

for anchor_tag in anchor_tags:
    anchor_tag_href = anchor_tag.get('href', None)
    links.append(anchor_tag_href)

print(links)

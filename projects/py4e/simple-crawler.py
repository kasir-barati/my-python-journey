import re
import urllib.request

# Used re.compile() to save the resulting regular expression object for reuse. More efficient when the expression since we will reuse it several times.
# Note: Here we are using "raw string notation".
# Learn more about raw string notions: https://docs.python.org/3/library/re.html#module-re
url_re = re.compile(
    r'\b(?:https?://|www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:/[^\s]*)?\b'
)
url_cleaner_re = re.compile(r'[^a-zA-Z0-9/_-]+$')


def url_finder(data):
    # Find all URLs in the string
    urls = url_re.findall(data)
    # Clean URLs by removing trailing invalid characters
    # It will replace invalid chars with '' in the url variable, and if the url_cleaner_re could not match anything it will return the original string.
    cleaned_urls = [url_cleaner_re.sub('', url) for url in urls]

    return cleaned_urls


links = list()
# Note #1: You have to specify the protocol otherwise it will blow up!
# Note #2: if you try to open websites with SSL on them you'll get a 403!
response = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
for line in response:
    decoded_line = line.decode().strip()
    urls = url_finder(decoded_line)

    if (len(urls) > 0):
        # Extend the list by appending all the items from the iterable.
        # Equivalent to links[len(links):] = urls.
        links.extend(urls)

print(links)

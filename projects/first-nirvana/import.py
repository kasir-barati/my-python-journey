import re

text = "'I am not yelling', She said. Though we knew it to not be true."

result = re.sub('[a-z]', '', text)

print(result)
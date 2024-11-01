import os
import sys

try:
    os.system('clear')
except:
    print("Could not clear the console!")

print("""
    Word counter script:

    Exit codes meaning:
        1: file name was not entered.
        2: could not find the file.

""")
filename = input('Enter a file name: ')

if (len(filename) == 0):
    sys.exit(1)

try:
    file_handler = open(filename)
except Exception as exception:
    # Printing exception in the stderr since the default value is sys.stdout
    print(exception, file=sys.stderr)
    sys.exit(2)
else:
    print("File opened!")

word_counter = dict()

for line in file_handler:
    line = line.rstrip()
    words = line.split()
    for word in words:
        word_counter[word] = word_counter.get(word, 0) + 1

most_repeated_word_count = None

for count in word_counter.values():
    if (most_repeated_word_count == None or most_repeated_word_count < count):
        most_repeated_word_count = count

print("These words were repeated {} times".format(most_repeated_word_count))

for word, count in word_counter.items():
    if (count == most_repeated_word_count):
        print(f"    Word: {word}")

file_handler.close()
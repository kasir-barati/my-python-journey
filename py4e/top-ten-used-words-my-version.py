import os
import sys

try:
    os.system('clear')
except:
    print('Could not the screen!', file=sys.stderr)

print("""
    Accept a file name and find top ten most used words.
    
    Exit codes meaning:
        1: No file name.
        2: Any error from the time we attempt to open the file and process it.
""")

filename = input("Enter file name: ")

if (len(filename) == 0):
    sys.exit(1)

def find_top_ten_words(words):
    result = {}
    reversed_words = {}

    # Sort a dictionary based on values or keys: 
    # https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
    for key, value in words.items():
        reversed_words[value] = key
    
    # Here is where I implement it a bit immature!
    reversed_sorted_values = sorted(reversed_words, reverse=True)
    for value in reversed_sorted_values[:10]:
        result[reversed_words[value]] = value
        del reversed_words[value]

    return result

def word_counter(file):
    result = dict()
    
    for line in file:
        words = line.split()
        for word in words:
            result[word] = result.get(word, 0) + 1
    
    return result

def read_file(file_path, callback_function):
    try:
        with open(file_path) as file:
            return callback_function(file)
    except Exception as exception:
        print(exception, file=sys.stderr)
        sys.exit(2)

words = read_file(filename, word_counter)
top_ten_words = find_top_ten_words(words)

print("Top ten words in the file are:", top_ten_words)
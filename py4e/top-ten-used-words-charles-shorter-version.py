# Lambda version

file_handle = open('intro.txt')
word_counter = dict()
for line in file_handle:
    words = line.split()
    for word in words: 
        word_counter[word] = word_counter.get(word, 0) + 1

reversed_word_counter = [ (value, key) for key, value in word_counter.items() ]
sorted_reversed_word_counter = sorted(reversed_word_counter, reverse=True)

for value, key in sorted_reversed_word_counter[:10]:
    print(key, value)
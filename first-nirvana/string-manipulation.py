full_name = 'Kasir' + ' ' + 'Barati'
print(full_name)

message = 'This ' + str(6) + ' is not ' + 'buggy'
print(message) # This 6 is not buggy

names = 'Kasir,Mohammad Jawad'
print(names.split(',')) # ['Kasir', 'Mohammad Jawad']
names = 'Kasir,Mohammad Jawad,Kasir San'
print(names.split(',', 1)) # ['Kasir', 'Mohammad Jawad,Kasir San']

# Wrong usage

message = 'This ' + 6 + ' is ' + 'buggy'
print(message) # TypeError: can only concatenate str (not "int") to str
file = open('names.txt', 'rt')

text = file.read()

file.close()

names = text.split(', ')

for name in names:
    print(name)

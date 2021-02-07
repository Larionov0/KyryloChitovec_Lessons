file = open('secret.txt', 'rt')

text1 = file.readline()
print(text1)
text2 = file.readline()
print(text2)
text3 = file.read()
print(text3)

file.close()

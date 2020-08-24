import fileinput, random 

path = "/usr/share/dict/words"
words = list(fileinput.input(path))

print(random.choice(words))
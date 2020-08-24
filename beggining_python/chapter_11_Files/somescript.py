import sys
text = sys.stdin.read()
words = text.split()
wcount = len(words)
print("Wordcount: ", wcount)
freq = {}
text = input('> ')
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
words = freq.keys()
sorted(words)

for w in words:
    print("%s:%d" % (w, freq[w]))

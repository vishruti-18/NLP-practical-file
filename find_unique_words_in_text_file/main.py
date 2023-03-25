text_file = open('data.txt', 'r')
text = text_file.read()

#cleaning
text = text.lower()
words = text.split()
words = [word.strip(""" "'.,!;()[]'" """) for word in words]
words = [word.replace("'s", '') for word in words]

#finding unique
unique = list(set(words))

#sort
unique.sort()

#print
print(unique)
import nltk

# Sample text
text = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog again."

# Tokenize the text into individual words
words = nltk.word_tokenize(text)

# Calculate the type-token ratio
ttr = len(set(words)) / len(words)

# Print the result
print("Type-Token Ratio:", ttr)
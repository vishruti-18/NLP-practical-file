import nltk
from nltk.tokenize import word_tokenize
from nltk import ngrams

# Sample text
text = "The quick brown fox jumps over the lazy dog"

# Tokenize the text into individual words
tokens = word_tokenize(text)

# Generate bi-grams
bigrams = list(ngrams(tokens, 2))

# Generate tri-grams
trigrams = list(ngrams(tokens, 3))

# Print the bi-grams
print("Bi-grams:")
for bg in bigrams:
    print(bg)

# Print the tri-grams
print("\nTri-grams:")
for tg in trigrams:
    print(tg)

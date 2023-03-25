import nltk
import random

# Sample corpus
text_file = open('data.txt', 'r')
corpus = text_file.read()

# Tokenize the corpus into individual words
tokens = nltk.word_tokenize(corpus)

# Create a bigram model from the tokens
bigrams = nltk.bigrams(tokens)
model = nltk.ConditionalFreqDist(bigrams)

# Generate a vocabulary of 10 words
vocabulary_size = 40
vocabulary = []


while len(vocabulary) < vocabulary_size:
    if len(vocabulary) == 0:
        start_word = random.choice(tokens)
    else:
        start_word = vocabulary[-1]
    freq_dist = model[start_word]

    if freq_dist.N() == 0:
        start_word = random.choice(tokens)
        freq_dist = model[start_word]
    max_freq = freq_dist.N()
    random_freq = random.randint(1, max_freq)
    cumulative_freq = 0
    
    for word in freq_dist:
        cumulative_freq += freq_dist[word]
        if cumulative_freq >= random_freq:
            start_word = word
            break
    
    vocabulary.append(start_word)

# Print the generated vocabulary
print("Generated vocabulary:", " ".join(vocabulary))
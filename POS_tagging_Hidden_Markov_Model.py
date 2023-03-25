import nltk
# from nltk.corpus import brown

nltk.dwonload('brown')

# create a training corpus
corpus = brown.tagged_sents()

# create a vocabulary set
vocab = set([word.lower() for sentence in corpus for (word, tag) in sentence])

# define the tags
tags = set([tag for sentence in corpus for (word, tag) in sentence])

# create the transition matrix
transitions = {}
for sentence in corpus:
    for i in range(len(sentence)-1):
        tag1 = sentence[i][1]
        tag2 = sentence[i+1][1]
        if tag1 in transitions:
            if tag2 in transitions[tag1]:
                transitions[tag1][tag2] += 1
            else:
                transitions[tag1][tag2] = 1
        else:
            transitions[tag1] = {tag2: 1}

# normalize the transition matrix
for tag1 in transitions:
    total = sum(transitions[tag1].values())
    for tag2 in transitions[tag1]:
        transitions[tag1][tag2] /= total

# create the emission matrix
emissions = {}
for sentence in corpus:
    for token, tag in sentence:
        if tag in emissions:
            if token.lower() in emissions[tag]:
                emissions[tag][token.lower()] += 1
            else:
                emissions[tag][token.lower()] = 1
        else:
            emissions[tag] = {token.lower(): 1}

# normalize the emission matrix
for tag in emissions:
    total = sum(emissions[tag].values())
    for token in emissions[tag]:
        emissions[tag][token] /= total

# create the HMM model


def hmm_model(sentence):
    tokens = sentence.lower().split()
    viterbi = []
    backpointer = []
    first_viterbi = {}
    first_backpointer = {}
    for tag in tags:
        if tag != ".":
            first_viterbi[tag] = transitions["."][tag] * \
                emissions[tag].get(tokens[0], 0)
            first_backpointer[tag] = "."
    viterbi.append(first_viterbi)
    backpointer.append(first_backpointer)
    for t in range(1, len(tokens)):
        viterbi_t = {}
        backpointer_t = {}
        for tag in tags:
            if tag != ".":
                max_prob = 0
                max_backpointer = None
                for prev_tag in tags:
                    prob = viterbi[t-1][prev_tag] * transitions[prev_tag].get(
                        tag, 0) * emissions[tag].get(tokens[t], 0)
                    if prob > max_prob:
                        max_prob = prob
                        max_backpointer = prev_tag
                viterbi_t[tag] = max_prob
                backpointer_t[tag] = max_backpointer
        viterbi.append(viterbi_t)
        backpointer.append(backpointer_t)
    last_viterbi = {}
    last_backpointer = {}
    for tag in tags:
        if tag != ".":
            last_viterbi[tag] = viterbi[-1][tag] * transitions[tag]["."]
            last_backpointer[tag] = max(
                tags, key=lambda prev_tag: viterbi[-1][prev_tag] * transitions[prev_tag].get(tag, 0))
    viterbi.append(last_viterbi)
    backpointer.append(last_backpointer)
    max_prob = max(last_viterbi.values())
    max_backpointer = max(last_viterbi, key=last_viterbi)
    current_backpointer = max_backpointer
    reversed_path = [max_backpointer]
    for bp in reversed(backpointer[:-1]):
        reversed_path.append(bp[current_backpointer])
        current_backpointer = bp[current_backpointer]
    path = list(reversed(reversed_path))
    return list(zip(tokens, path))

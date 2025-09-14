# Problem10: Given a sentence, count the frequency of each word ignoring case and punctuation.

import string

def word_freq(sentence):
    translator = str.maketrans('', '', string.punctuation)
    sentence = sentence.translate(translator).lower()
    words = sentence.split()
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    return freq

print(word_frequency("hello, hello! How are you? Are you fine?"))

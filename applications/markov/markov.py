import random

"""
Understand:
    go through file, for each word keep track of the words 
    that are after each apperence of the word use that info to make random sentences
Plan:
    - open and read file
    - split the output into an array of words to grab individual words
    - create empty cache
    - create empty start words list
    - create empty stop words list
    - loop through each word in the words array 
    - if the word isn't in cache, add it as key and value is what comes after the word
    - if the word is a start word add it to the start array
    - if the word is a stop word add it to the stop array
    - if the word is in the cache, add the word that comes after to existing value for given key
    - pick a random "start" word
    - loop through, print a word
    - if the word is a stop word stop
    - otherwise pick a word that can follow it

    start words begin with a capital, or a " followed by a capital.
    Stop words are words that end in any of the punctuation '.?!', or that punctuation followed by a ".
"""

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

    words_split = words.split()
    print(words)

# TODO: analyze which words can follow other words
# Your code here
cache = {}
start_words = []
stop_words = []

def cache_words():
    for i, word in enumerate(words_split):
        if i < len(words_split) - 1:
            if isStarting(word):
                start_words.append(word)
            if isStopping(word):
                stop_words.append(word)
            if word not in cache:
                cache[word] = []
            cache[word].append(words_split[i+1])

def isStarting(word):
    if word[0].isupper():
        return True
    elif word[0] == '"' and word[1].isupper():
        return True
    else:
        return False    

def isStopping(word):
    if word.endswith(("!", "?", ".")):
        return True
    elif word.endswith('"') and word[:-1].endswith(("!", "?", ".")):
        return True
    else:
        return False    

# TODO: construct 5 random sentences
# Your code here
cache_words()
for i in range(5):
    print(f"Sentence #{i + 1}:")
    word = random.choice(start_words)
    print(word, end = " ")
    while not isStopping(word):
        word = random.choice(cache[word])
        print(word, end = " ")
    print("\n")

import re

def word_count(s):
    # Your code here

    
    d = {}
    
    # create an array of words that includes [a-zA-Z0-9_] + apostrophes before word characters
    words = re.findall(r"\w+(?:'\w+)?", s)

    # for each word in words array
    for word in words:
        # check if the word lowercased is in the dictionary
        if word.lower() not in d:
            # add it and set it's value to 1 if it's not there already
            d[word.lower()] = 1
        # if it exists add 1 to count
        else:
            d[word.lower()] += 1

    return d




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))